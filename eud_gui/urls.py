from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # By including without a tuple, the patterns are added directly to the global space
    # but prefixed with 'api/'.
    path('', include('apps.core.urls')),
    path('api/', include('apps.generic_crud.urls')),
    path('api/audit/', include('apps.audit.urls')),
    path('', include('apps.clients.urls')),
    path('le/', include('apps.clients_le.urls')),
    path('repapering/', include('apps.repapering.urls')),
    path('users/', include('apps.users.urls')),
    path('dashboard/', include('apps.dashboard_bots.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
