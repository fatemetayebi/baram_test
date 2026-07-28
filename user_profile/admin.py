from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('-date_joined',)
    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('username', 'email', 'phone_number')
        }),
        ('دسترسی‌ها', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'date_joined', 'last_login')


