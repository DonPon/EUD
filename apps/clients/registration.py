from apps.generic_crud.registry import CrudRegistry
from .models import Client, Nationality, Address, Communication, Portfolio, Account

def register_clients_models():
    """Register all Bank Client models for generic CRUD."""
    
    # 'fields' controls the API Serializer and Form
    # 'list_display' controls the DataTables columns
    
    CrudRegistry.register(Client, {
        'fields': ['id', 'client_uuid', 'first_name', 'last_name', 'br_number', 'date_of_birth', 'status', 'created_at'],
        'list_display': ['first_name', 'last_name', 'br_number', 'status', 'created_at'],
        'filter_fields': ['status', 'br_number'],
        'search_fields': ['first_name', 'last_name', 'br_number'],
        'exclude_from_info': ['id', 'client_uuid', 'created_at', 'updated_at'] # Example exclusion
    })
    
    CrudRegistry.register(Nationality, {
        'fields': ['id', 'client_uuid', 'country', 'is_main', 'created_at'],
        'list_display': ['country', 'is_main'],
        'filter_fields': ['client_uuid', 'is_main'],
        'search_fields': ['country', 'is_main'],
    })
    
    CrudRegistry.register(Address, {
        'fields': ['id', 'client_uuid', 'street', 'city', 'zip_code', 'country', 'is_main', 'is_domicile', 'is_tax_domicile', 'tin', 'created_at'],
        'list_display': ['street', 'city', 'country', 'is_main', 'is_domicile', 'is_tax_domicile', 'tin'],
        'filter_fields': ['client_uuid', 'is_main', 'is_domicile', 'is_tax_domicile'],
        'search_fields': ['street', 'city', 'country', 'is_main', 'is_domicile', 'is_tax_domicile', 'tin'],
    })
    
    CrudRegistry.register(Communication, {
        'fields': ['id', 'client_uuid', 'comm_type', 'value', 'is_main', 'created_at'],
        'list_display': ['comm_type', 'value', 'is_main'],
        'filter_fields': ['client_uuid', 'comm_type', 'is_main'],
        'search_fields': ['comm_type', 'value', 'is_main'],
    })
    
    CrudRegistry.register(Portfolio, {
        'fields': ['id', 'client_uuid', 'portfolio_number', 'name', 'created_at'],
        'list_display': ['portfolio_number', 'name'],
        'filter_fields': ['client_uuid', 'portfolio_number'],
        'search_fields': ['portfolio_number', 'name'],
    })
    
    CrudRegistry.register(Account, {
        'fields': ['id', 'client_uuid', 'portfolio_uuid', 'portfolio_info', 'account_number', 'currency', 'balance', 'created_at'],
        'list_display': ['account_number', 'portfolio_info', 'currency', 'balance'],
        'filter_fields': ['client_uuid', 'portfolio_uuid', 'currency'],
        'search_fields': ['account_number', 'currency', 'balance'],
    })
