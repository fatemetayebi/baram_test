from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_days', 'is_active')
    list_filter = ('service_type', 'is_active')
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'service_type', 'description')


