from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.english_index_view, name='index'),
    path('fa/', views.persian_index_view, name='persian_index'),
    path('en/', views.english_index_view, name='english_index'),
    path('', include('core.urls')),
]
