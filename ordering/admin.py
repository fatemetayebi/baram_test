from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'order_status', 'order_date')
    list_filter = ('order_status', 'order_date')
    search_fields = ('user__username', 'service__name')
    ordering = ('-order_date',)
    fields = ('user', 'service', 'order_status', 'order_date')
