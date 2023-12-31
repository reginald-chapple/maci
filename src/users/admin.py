from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User, Client

admin.site.register(Client)

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': (
            'name', 
            'phone_number', 
            'birthdate',
            'gender', 
            'photo',
            'address', 
            'city',
            'state', 
            'country',
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_provider', 'is_client', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'name', 'is_staff', 'is_provider', 'is_client',)
    list_filter = ('is_staff', 'is_provider', 'is_client',)
    search_fields = ('username', 'email', 'name',)
    ordering = ('username',)
