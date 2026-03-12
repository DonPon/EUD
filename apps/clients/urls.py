from django.urls import path
from .views import ClientListView, ClientDetailView

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('clients/<uuid:client_uuid>/', ClientDetailView.as_view(), name='detail'),
]
