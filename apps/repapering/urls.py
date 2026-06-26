from django.urls import path
from . import views

app_name = 'repapering'

urlpatterns = [
    path('', views.ScenarioListView.as_view(), name='scenario_list'),
    path('scenario/<int:pk>/', views.ScenarioDetailView.as_view(), name='scenario_detail'),
    path('requirement/<int:pk>/delete/', views.DocumentRequirementDeleteView.as_view(), name='requirement_delete'),
]
