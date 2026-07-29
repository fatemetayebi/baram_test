from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Service
from .serializers import (
    ServiceSerializer,
    ServiceListSerializer,
    ServiceCreateUpdateSerializer
)
from .filters import ServiceFilter
from rest_framework.permissions import IsAuthenticated, AllowAny


class ServicePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'


class IsRoleAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, 'role', None) == 'admin'
        )


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ServiceFilter
    search_fields = ['name', 'description']
    ordering = ['name']
    pagination_class = ServicePagination

    def get_queryset(self):
        queryset = Service.objects.all()

        if self.request.user and self.request.user.is_authenticated and self.request.user.is_admin:
            return queryset

        return queryset.filter(is_active=True)


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsRoleAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        service = serializer.instance
        output_serializer = ServiceSerializer(service)

        return Response({
            'message': 'Service successfully created',
            'service': output_serializer.data
        }, status=status.HTTP_201_CREATED)


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsRoleAdmin]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Return full data
        output_serializer = ServiceSerializer(instance)

        return Response({
            'message': 'Service successfully updated',
            'service': output_serializer.data
        })


class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated, IsRoleAdmin]
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        service_name = instance.name
        self.perform_destroy(instance)

        return Response({
            'message': f'Service "{service_name}" successfully deleted'
        }, status=status.HTTP_200_OK)


