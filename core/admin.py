from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at', 'email')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    
    # Optional: customize how messages are displayed
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')

    # Optional: add actions
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        # You can extend this if you add a 'read' field to the model
        queryset.update(status='read')
    mark_as_read.short_description = "Mark selected messages as read"