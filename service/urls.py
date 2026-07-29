from django.urls import path
from service.views import *

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<int:id>/', ServiceDetailView.as_view(), name='service_detail'),
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('update/<int:id>/', ServiceUpdateView.as_view(), name='service_update'),
    path('delete/<int:id>/', ServiceDeleteView.as_view(), name='service_delete'),
]
