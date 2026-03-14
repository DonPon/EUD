from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('bots-partial/', views.DashboardBotsPartialView.as_view(), name='bots_partial'),
    path('bot/<str:bot_name>/', views.BotDetailsView.as_view(), name='bot_details'),
]
