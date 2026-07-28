from django.contrib import admin
from .models import Service, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_days', 'is_active')
    list_filter = ('service_type', 'is_active')
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'service_type', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'order_status', 'order_date')
    list_filter = ('order_status', 'order_date')
    search_fields = ('user__username', 'service__name')
    ordering = ('-order_date',)
    fields = ('user', 'service', 'order_status', 'order_date')