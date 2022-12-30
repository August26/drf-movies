from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'^rest-auth/', include('rest_auth.urls')),
    path(r'^api/auth/', include('rest_framework.urls')),
    #path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include(router.urls))
]
