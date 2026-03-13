from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # By including without a tuple, the patterns are added directly to the global space
    # but prefixed with 'api/'.
    path('api/', include('apps.generic_crud.urls')),
    path('api/audit/', include('apps.audit.urls')),
    path('', include('apps.clients.urls')),
    path('users/', include('apps.users.urls')),
    path('dashboard/', include('apps.dashboard_bots.urls')),
]
