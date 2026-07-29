from django.db import models

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

