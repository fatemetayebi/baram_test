from rest_framework import viewsets, status, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order
from .serializers import OrderListSerializer, OrderDetailSerializer, OrderCreateSerializer



class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not (request.user and request.user.is_authenticated):
            return False
        return getattr(request.user, 'role', None) == 'Admin' or obj.user == request.user


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related('user', 'service')
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['service__name', 'user__username']
    ordering_fields = ['order_date']
    ordering = ['-order_date']

    def get_serializer_class(self):
        if self.action in ['update', 'create']:
            return OrderCreateSerializer
        elif self.action == 'list':
            return OrderListSerializer
        return OrderDetailSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Order.objects.none()

        # Separate access levels based on role
        if getattr(user, 'role', None) == 'Admin':
            return Order.objects.all().select_related('user', 'service')

        return Order.objects.filter(user=user).select_related('user', 'service')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        return Response({
            'message': 'Order successfully created',
            'order': OrderDetailSerializer(order).data,
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'message': 'Order successfully updated',
            'order': OrderDetailSerializer(instance).data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.order_status not in ['pending', 'rejected']:
            return Response({
                'error': 'Cannot delete order with current status'
            }, status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        return Response({
            'message': f'Order  successfully deleted'
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='my-orders')
    def my_orders(self, request):
        orders = self.get_queryset().filter(user=request.user)
        queryset = self.filter_queryset(orders)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OrderListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='my-statistics')
    def my_statistics(self, request):
        orders = Order.objects.filter(user=request.user)
        total_orders = orders.count()
        last_order = orders.order_by('-order_date').first()

        return Response({
            'total_orders': total_orders,
            'last_order': OrderDetailSerializer(last_order).data if last_order else None
        })
