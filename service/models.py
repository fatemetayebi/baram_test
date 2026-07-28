from django.db import models
from user_profile.models import User


class Service(models.Model):
    class ServiceTypeChoices(models.TextChoices):
        SEO = 'سئو'
        WEBSITE_DESIGN = 'طراحی وبسایت'
        SOFTWARE_DEV = 'توسعه نرم افزار'
        OTHER='سایر'

    name = models.CharField(max_length=200, verbose_name='Service Name')
    service_type = models.CharField(
        max_length=20,
        choices=ServiceTypeChoices.choices,
        default=ServiceTypeChoices.OTHER,
        verbose_name='Service Type'
    )

    description = models.TextField(null=True, blank=True,verbose_name='Description')
    duration_days = models.PositiveIntegerField(
        verbose_name='Duration (Days)',
        default=1,
        help_text='Time required to complete the service in days'
    )
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['name']
        unique_together = ['name', 'service_type']

    def __str__(self):
        return f"{self.name} - {self.service_type}"



class Order(models.Model):
    class OrderStatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending Approval'
        CONFIRMED = 'confirmed', 'Confirmed'
        REJECTED = 'rejected', 'Rejected'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='User')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='orders', verbose_name='Service')
    order_status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
        verbose_name='Order Status'
    )
    description = models.TextField(null=True, blank=True, verbose_name='Order Description')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-order_date']

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.service.name}"