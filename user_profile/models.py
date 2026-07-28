from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        CUSTOMER = 'customer', 'Customer'
        SUPPORT = 'support', 'Support'

    role = models.CharField(max_length=20, choices=RoleChoices.choices, default=RoleChoices.CUSTOMER, verbose_name='User Role')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone Number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    @property
    def is_admin(self):
        return self.role == self.RoleChoices.ADMIN

    @property
    def is_staff_user(self):
        return self.role in [self.RoleChoices.ADMIN, self.RoleChoices.STAFF]




