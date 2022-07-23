from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from user_selection.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
