from apps.generic_crud.registry import CrudRegistry
from .models import Bot, BotStatus, BotRecord

def register_dashboard_models():
    """Register all Dashboard models for generic CRUD."""
    
    CrudRegistry.register(Bot, {
        'fields': ['id', 'name', 'description', 'created_at'],
        'list_display': ['name', 'description'],
        'search_fields': ['name', 'description'],
        'is_client_related': False
    })
    
    CrudRegistry.register(BotStatus, {
        'fields': ['id', 'bot', 'bot_status', 'created_at'],
        'list_display': ['bot', 'bot_status'],
        'filter_fields': ['bot_status'],
        'is_client_related': False
    })
    
    CrudRegistry.register(BotRecord, {
        'section': ['np', 'le'],
        'fields': [
            'id', 'bot_name', 'bank_rel', 'start_time', 'end_time', 
            'status', 'message', 'client_type', 't_number', 'run_identifier', 
            'modified', 'created'
        ],
        'list_display': ['bot_name', 'bank_rel', 'status', 'created'],
        'filter_fields': ['bot_name', 'status', 'bank_rel'],
        'client_filter_field': 'bank_rel',
        'search_fields': ['bot_name', 'bank_rel', 'message', 'status', 'client_type'],
        'read_only': True
    })
