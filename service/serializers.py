from rest_framework import serializers
from .models import Service
from django.core.exceptions import ValidationError


class ServiceSerializer(serializers.ModelSerializer):
    service_type_display = serializers.CharField(
        source='get_service_type_display',
        read_only=True
    )

    class Meta:
        model = Service
        fields = (
            'id', 'name', 'service_type', 'service_type_display',
            'description', 'duration_days', 'is_active',
            'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at', 'id')


    def validate(self, data):
        if self.instance:
            existing = Service.objects.filter(
                name=data.get('name', self.instance.name),
                service_type=data.get('service_type', self.instance.service_type)
            ).exclude(id=self.instance.id)
        else:
            existing = Service.objects.filter(
                name=data.get('name'),
                service_type=data.get('service_type')
            )

        if existing.exists():
            raise serializers.ValidationError(
                'A service with this name and type already exists'
            )
        return data


class ServiceListSerializer(serializers.ModelSerializer):

    service_type_display = serializers.CharField(
        source='get_service_type_display',
        read_only=True
    )

    class Meta:
        model = Service
        fields = (
            'id', 'name', 'service_type', 'service_type_display',
            'duration_days', 'is_active'
        )


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'service_type', 'description','is_active')

    def validate(self, data):
        # Validate duplicate entries
        if Service.objects.filter(
                name=data.get('name'),
                service_type=data.get('service_type')
        ).exists():
            raise serializers.ValidationError(
                'A service with this name and type already exists'
            )
        return data
