from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'contact-name', 
                'placeholder': 'Name',
                'autocomplete': 'on'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'id': 'contact-email', 
                'placeholder': 'Email',
                'autocomplete': 'on'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'contact-subject', 
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'contact-message', 
                'placeholder': 'Message',
                'rows': 5
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
