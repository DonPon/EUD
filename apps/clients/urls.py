from django.urls import path
from .views import ClientListView, ClientDetailView, CompleteReviewView

app_name = 'clients'

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='list'),
    path('clients/<uuid:client_uuid>/', ClientDetailView.as_view(), name='detail'),
    path('clients/<uuid:client_uuid>/complete-review/', CompleteReviewView.as_view(), name='complete-review'),
]
