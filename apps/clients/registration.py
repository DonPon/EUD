from apps.generic_crud.registry import CrudRegistry
from .models import (
    BankingRelationship, AdditionalFormDE, PersonalInformation, Address,
    Communication, ClientAdvisor, Nationality, TIN, EBanking,
    Product, MeetingPreparation, Relationship, Account
)

def register_clients_models():
    """Register all Bank Client models for generic CRUD."""
    
    CrudRegistry.register(BankingRelationship, {
        'fields': [
            'id', 'client_uuid', 'banking_relationship', 'technical_account', 'additional_br',
            'distribution_list', 'name_of_banking_relationship', 'type_of_account',
            'type_of_signature', 'client_segment', 'code_ksc', 'recording_phone_calls',
            'declaration_email', 'language', 'opened_in_ubs_premises', 'instructions',
            'account_and_securities_statements', 'type_and_purpose',
            'agreement_distribution_fees', 'send_documents', 'csc', 'ateco', 'sae',
            'level_of_professionalism', 'number_of_portfolios', 'created_at'
        ],
        'list_display': ['name_of_banking_relationship', 'banking_relationship', 'type_of_account', 'client_segment'],
        'filter_fields': ['type_of_account', 'client_segment', 'code_ksc', 'language'],
        'search_fields': ['name_of_banking_relationship', 'banking_relationship'],
    })

    CrudRegistry.register(PersonalInformation, {
        'fields': [
            'id', 'client_uuid', 'first_name', 'last_name', 'date_of_birth',
            'place_of_birth', 'country_of_birth', 'marital_status', 'occupation_sector',
            'fiscal_identifier', 'indication_tin', 'sensitive_client'
        ],
        'list_display': ['first_name', 'last_name', 'date_of_birth', 'marital_status'],
        'filter_fields': ['marital_status', 'sensitive_client'],
        'search_fields': ['first_name', 'last_name', 'fiscal_identifier'],
    })

    CrudRegistry.register(Nationality, {
        'fields': [
            'id', 'client_uuid', 'is_main_nationality', 'nationality', 'nci', 'id_type',
            'fiscal_code', 'release_authority', 'release_date', 'expiry_date'
        ],
        'list_display': ['nationality', 'is_main_nationality', 'id_type', 'expiry_date'],
        'filter_fields': ['is_main_nationality', 'id_type'],
    })

    CrudRegistry.register(Address, {
        'fields': [
            'id', 'client_uuid', 'person_entity', 'type_of_address', 'first_name', 'last_name',
            'street', 'no', 'postal_code', 'city', 'province', 'country', 'documents_sent'
        ],
        'list_display': ['type_of_address', 'city', 'country', 'documents_sent'],
        'filter_fields': ['type_of_address', 'country'],
        'search_fields': ['city', 'street', 'last_name'],
    })

    CrudRegistry.register(TIN, {
        'fields': ['id', 'client_uuid', 'aei_tin'],
        'list_display': ['aei_tin'],
    })

    CrudRegistry.register(Communication, {
        'fields': [
            'id', 'client_uuid', 'first_and_last_name', 'landline', 'phone', 'phone_number',
            'mobile_number', 'email_address', 'fax_address', 'pec_address'
        ],
        'list_display': ['first_and_last_name', 'phone_number', 'email_address'],
        'search_fields': ['first_and_last_name', 'email_address'],
    })

    CrudRegistry.register(EBanking, {
        'fields': ['id', 'client_uuid', 'has_ebanking', 'contract_number'],
        'list_display': ['has_ebanking', 'contract_number'],
    })

    CrudRegistry.register(Relationship, {
        'fields': [
            'id', 'client_uuid', 'child_unique_id', 'type_of_relationship',
            'type_of_access', 'level_of_access', 'relation_with_owner'
        ],
        'list_display': ['client_uuid', 'child_unique_id', 'type_of_relationship', 'relation_with_owner'],
        'filter_fields': ['type_of_relationship'],
    })

    CrudRegistry.register(Product, {
        'fields': ['id', 'client_uuid', 'product_name', 'product_id', 'status'],
        'list_display': ['product_name', 'product_id', 'status'],
        'filter_fields': ['status'],
    })

    CrudRegistry.register(Account, {
        'fields': ['id', 'client_uuid', 'product_uuid', 'product_info', 'account_number', 'currency', 'balance', 'created_at'],
        'list_display': ['account_number', 'product_info', 'currency', 'balance'],
        'filter_fields': ['client_uuid', 'product_uuid', 'currency'],
        'search_fields': ['account_number', 'currency', 'balance'],
    })

    CrudRegistry.register(ClientAdvisor, {
        'fields': ['id', 'client_uuid', 'first_name', 'last_name', 'email', 'desk', 'branch', 'role'],
        'list_display': ['last_name', 'first_name', 'role', 'branch'],
        'filter_fields': ['role', 'branch'],
    })

    CrudRegistry.register(MeetingPreparation, {
        'fields': [
            'id', 'client_uuid', 'place', 'date_of_meeting', 'time',
            'hospitality', 'performance_since_beginning'
        ],
        'list_display': ['date_of_meeting', 'time', 'place', 'hospitality'],
    })

    CrudRegistry.register(AdditionalFormDE, {
        'fields': [
            'id', 'client_uuid', 'request_to_become_professional', 'forward_trading_transactions',
            'exemption_order', 'last_name', 'first_name', 'identification_number',
            'date_of_birth', 'amount', 'timeline', 'execution', 'until_canceled',
            'limited_power_of_attorney', 'poa_all_accounts', 'poa_in_case_of_death',
            'tax_at_source_canada', 'ubs_digital_banking_authorization'
        ],
        'list_display': ['last_name', 'first_name', 'identification_number', 'amount'],
        'filter_fields': ['amount', 'execution'],
    })
