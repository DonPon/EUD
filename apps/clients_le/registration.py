from apps.generic_crud.registry import CrudRegistry
from .models import LE_BankingRelationship, LE_Information, LE_Address, LE_Communication

def register_le_clients_models():
    """Register all Legal Entity models for generic CRUD."""
    
    CrudRegistry.register(LE_BankingRelationship, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'legal_name', 'banking_relationship', 
            'technical_account', 'client_segment', 'code_ksc', 
            'language', 'status', 'created_at'
        ],
        'list_display': ['legal_name', 'banking_relationship', 'client_segment', 'status'],
        'filter_fields': ['client_segment', 'code_ksc', 'language'],
        'search_fields': ['legal_name', 'banking_relationship'],
    })

    CrudRegistry.register(LE_Information, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'legal_name', 'legal_form', 'registration_number',
            'country_of_registration', 'date_of_registration', 'tax_id', 
            'lei_code', 'industry_sector', 'website'
        ],
        'list_display': ['legal_name', 'legal_form', 'registration_number', 'lei_code'],
        'filter_fields': ['legal_form', 'country_of_registration'],
        'search_fields': ['legal_name', 'registration_number', 'tax_id'],
    })

    CrudRegistry.register(LE_Address, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'type_of_address', 'street', 'no', 
            'postal_code', 'city', 'province', 'country'
        ],
        'list_display': ['type_of_address', 'city', 'country'],
        'filter_fields': ['type_of_address', 'country'],
    })

    CrudRegistry.register(LE_Communication, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'department', 'contact_person', 
            'phone_number', 'email_address', 'fax_address', 'pec_address'
        ],
        'list_display': ['contact_person', 'department', 'phone_number', 'email_address'],
    })
