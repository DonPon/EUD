from apps.generic_crud.registry import CrudRegistry
from django.contrib.auth import get_user_model

User = get_user_model()

def register_users_models():
    """Register User model for generic CRUD."""
    
    CrudRegistry.register(User, {
        'fields': ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined'],
        'list_display': ['username', 'email', 'role', 'is_active', 'is_staff'],
        'filter_fields': ['role', 'is_active', 'is_staff'],
        'search_fields': ['username', 'email', 'first_name', 'last_name'],
        'is_client_related': False
    })
