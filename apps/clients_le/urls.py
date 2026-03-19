from django.urls import path
from .views import LE_ClientListView, LE_ClientDetailView, BulkStatusUpdateLEView, LE_CompleteReviewView

app_name = 'clients_le'

urlpatterns = [
    path('', LE_ClientListView.as_view(), name='list'),
    path('bulk-status-update/', BulkStatusUpdateLEView.as_view(), name='bulk-status-update'),
    path('<uuid:client_uuid>/complete-review/', LE_CompleteReviewView.as_view(), name='complete-review'),
    path('<uuid:client_uuid>/', LE_ClientDetailView.as_view(), name='detail'),
]
