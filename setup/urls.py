# setup/urls.py
"""Main URL configuration for the project."""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API documentation routes (optional)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),

    # Browsable API login/logout URLs
    path('api-auth/', include('rest_framework.urls')),

    # App routes
    path('', include('posts.urls')),
]
