from django_filters import rest_framework as filters
from .models import Service


class ServiceFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Search in name'
    )

    service_type = filters.ChoiceFilter(
        choices=Service.ServiceTypeChoices.choices,
        label='Service type'
    )

    service_types = filters.MultipleChoiceFilter(
        field_name='service_type',
        choices=Service.ServiceTypeChoices.choices,
        label='Service types'
    )

    # Filter by active status
    is_active = filters.BooleanFilter(
        field_name='is_active',
        label='Active status'
    )


    class Meta:
        model = Service
        fields = ['name', 'service_type', 'service_types', 'is_active']
