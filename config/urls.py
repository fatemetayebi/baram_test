from django.contrib import admin
from django.urls import path, include
from user_profile import urls as user_profile_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(user_profile_urls)),
]
