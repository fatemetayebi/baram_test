from django.db import models
from user_profile.models import User
from service.models import Service

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