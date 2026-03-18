from django.urls import path
from rest_framework import routers
from .registry import CrudRegistry
from .views import DynamicViewSetFactory, RegistryMetadataView, GenericFormView

router = routers.DefaultRouter()
router.register(r'registry', RegistryMetadataView, basename='registry')

def register_all_viewsets():
    """Dynamically register all models in the CrudRegistry to the router."""
    registered_models = CrudRegistry.get_registered_models()
    for name, details in registered_models.items():
        model_class = details['model']
        config = details['config']
        viewset = DynamicViewSetFactory.create_viewset(model_class, config)
        # Use a unique basename to avoid conflicts
        router.register(f'table/{name}', viewset, basename=f'table-{name}')

def get_urlpatterns():
    register_all_viewsets()
    
    patterns = [
        path('gui/<str:table_name>/add/', GenericFormView.as_view(), name='generic-add'),
        path('gui/<str:table_name>/<pk>/edit/', GenericFormView.as_view(), name='generic-edit'),
    ]
    # Add router URLs to the list
    patterns += router.urls
    return patterns

# This will be evaluated when the app is loaded
urlpatterns = get_urlpatterns()
