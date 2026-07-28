from django.urls import path
from user_profile.views import *


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='api_register'),
    path('login/', UserLoginAPIView.as_view(), name='api_login'),
    path('profile/', UserProfileAPIView.as_view(), name='api_profile'),
    path('dashboard/', UserDashboardAPIView.as_view(), name='api_dashboard'),
]