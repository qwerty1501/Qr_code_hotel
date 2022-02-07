from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from djoser.urls import authtoken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('server.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
