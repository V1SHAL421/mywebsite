"""Configuration of the administrative interface for microblogs"""
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users"""
    
    list_display = [
        'first_name', 'last_name', 'username', 'email', 'is_active'
    ]
# Register your models here.
