from django.urls import path, include
from rest_framework import routers
from .views import HistoryView, HistoryListView

router = routers.DefaultRouter()
router.register(r'', HistoryView, basename='history')

urlpatterns = [
    # GUI Route
    path('gui/<str:table_name>/', HistoryListView.as_view(), name='audit-list'),
    
    # API Routes
    path('', include(router.urls)),
]
