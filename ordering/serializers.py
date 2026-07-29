from rest_framework import serializers
from ordering.models import Order
from django.utils import timezone
from datetime import timedelta


class OrderListSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    order_status_display = serializers.CharField(source='get_order_status_display', read_only=True)

    class Meta:
        model = Order
        fields = (
            'id', 'service_name',
            'order_status', 'order_status_display', 'order_date'
        )


class OrderDetailSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    service_type = serializers.CharField(source='service.service_type', read_only=True)
    order_status_display = serializers.CharField(source='get_order_status_display', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Order
        fields = (
            'id','user', 'user_name', 'user_email',
            'service', 'service_name', 'service_type',
            'order_status', 'order_status_display', 'description', 'order_date'
        )


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('service', 'description')

    def validate(self, data):
        service = data.get('service')

        if not service:
            raise serializers.ValidationError('Service selection is required')

        if not service.is_active:
            raise serializers.ValidationError('This service is currently inactive')

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        service = validated_data.get('service')

        order = Order.objects.create(
            user=user,
            service=service,
            description=validated_data.get('description', ''),
            order_status=Order.OrderStatusChoices.PENDING,
        )
        return order
