from django.contrib import admin
from django.urls import path, include
from user_profile import urls as user_profile_urls
from service import urls as service_urls
from ordering import urls as ordering_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(user_profile_urls)),
    path('services/', include(service_urls)),
    path('orders/', include(ordering_urls)),
]
