from django.urls import path
from .views import UserListView

app_name = 'users'

urlpatterns = [
    path('management/', UserListView.as_view(), name='management'),
]
