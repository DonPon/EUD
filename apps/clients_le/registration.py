from apps.generic_crud.registry import CrudRegistry
from .models import LE_TIN, LE_Account, LE_BankingRelationship, LE_ClientAdvisor, LE_Company, LE_EBanking, LE_Address, LE_Communication, LE_MeetingPreparation, LE_Nationality, LE_PersonalInformation, LE_Product, LE_Relationship

def register_le_clients_models():
    """Register all Legal Entity models for generic CRUD."""
    
    CrudRegistry.register(LE_BankingRelationship, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'legal_name', 'banking_relationship',
            'technical_account', 'additional_br', 'distribution_list',
            'name_of_banking_relationship', 'type_of_account', 'type_of_signature',
            'client_segment', 'code_ksc', 'recording_phone_calls', 'declaration_email',
            'language', 'opened_in_ubs_premises', 'instructions',
            'account_and_securities_statements', 'type_and_purpose', 'specify',
            'reporting_obligation', 'earning_statement', 'fees', 'approval_of_branch_head',
            'fiscal_identifier', 'agreement_distribution_fees', 'share_of_distribution',
            'send_documents', 'cscatecosae', 'further_notes',
            'level_of_professionalism', 'number_of_portfolios', 'status', 'created_at'
        ],
        'list_display': ['legal_name', 'banking_relationship', 'client_segment', 'status'],
        'filter_fields': ['client_segment', 'code_ksc', 'language', 'type_and_purpose', 'reporting_obligation'],
        'search_fields': ['legal_name', 'banking_relationship', 'name_of_banking_relationship'],
    })

    CrudRegistry.register(LE_Company, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'type_of_company', 'name_of_company', 'ivacf', 'iva',
            'fiscal_code', 'lei_code', 'date_of_constitution', 'place_of_constitution',
            'fiscal_residence', 'turnover_id', 'cciaa_type', 'cciaa_number',
            'released_by', 'date_of_issue', 'form_of_legal_entity',
            'professional_client_fiduciary_uhnw', 'created_at'
        ],
        'list_display': ['name_of_company', 'type_of_company', 'lei_code', 'fiscal_residence'],
        'filter_fields': ['type_of_company', 'fiscal_residence', 'form_of_legal_entity'],
        'search_fields': ['name_of_company', 'lei_code', 'fiscal_code'],
    })

    CrudRegistry.register(LE_PersonalInformation, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'legal_name', 'legal_form', 'registration_number',
            'country_of_registration', 'date_of_registration', 'tax_id',
            'lei_code', 'industry_sector', 'website',
            # Personal Information Fields
            'first_name', 'last_name', 'first_and_last_name', 'name_at_birth',
            'federal_state', 'date_of_birth', 'place_of_birth', 'country_of_birth',
            'marital_status', 'occupation_sector', 'fiscal_identifier', 'indication_tin',
            'sensitive_client', 'executor', 'beneficial_owner', 'tef'
        ],
        'list_display': ['legal_name', 'legal_form', 'first_and_last_name', 'lei_code'],
        'filter_fields': ['legal_form', 'country_of_registration', 'sensitive_client', 'executor', 'beneficial_owner'],
        'search_fields': ['legal_name', 'registration_number', 'tax_id', 'first_name', 'last_name'],
    })

    CrudRegistry.register(LE_Nationality, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'is_main_nationality', 'nationality', 'nci', 'id_type',
            'fiscal_code', 'release_authority', 'release_date', 'expiry_date'
        ],
        'list_display': ['nationality', 'is_main_nationality', 'id_type', 'expiry_date'],
        'filter_fields': ['is_main_nationality', 'id_type'],
    })

    CrudRegistry.register(LE_Address, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'person_entity', 'type_of_address', 'first_name', 'last_name',
            'street', 'no', 'postal_code', 'city', 'province', 'country', 'documents_sent'
        ],
        'list_display': ['type_of_address', 'city', 'country', 'documents_sent'],
        'filter_fields': ['type_of_address', 'country'],
        'search_fields': ['city', 'street', 'last_name'],
    })

    CrudRegistry.register(LE_TIN, {
        'section': 'le',
        'fields': ['id', 'client_uuid', 'aei_tin'],
        'list_display': ['aei_tin'],
    })

    CrudRegistry.register(LE_Communication, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'first_and_last_name', 'landline', 'phone', 'phone_number',
            'mobile_number', 'email_address', 'fax_address', 'pec_address'
        ],
        'list_display': ['first_and_last_name', 'phone_number', 'email_address'],
        'search_fields': ['first_and_last_name', 'email_address'],
    })

    CrudRegistry.register(LE_EBanking, {
        'section': 'le',
        'fields': ['id', 'client_uuid', 'has_ebanking', 'contract_number'],
        'list_display': ['has_ebanking', 'contract_number'],
    })

    CrudRegistry.register(LE_Relationship, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'child_unique_id', 'type_of_relationship',
            'type_of_access', 'level_of_access', 'relation_with_owner'
        ],
        'list_display': [
            'related_banking_relationship',
            'related_name_of_banking_relationship',
            'related_first_name',
            'related_last_name',
            'type_of_relationship',
            'relation_with_owner'
        ],
        'filter_fields': ['type_of_relationship'],
    })

    CrudRegistry.register(LE_Product, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'portfolio_id', 'portfolio_name', 'email_waiver',
            'reference_currency', 'investment_service', 'a_s_authorization_path',
            'investment_strategy', 'ip_risk_tolerance', 'investment_amount',
            'selected_service', 'all_in', 'sustainable_investing',
            'sustainability_preference', 'focus_equity', 'alternative_investment',
            'direct_instrument', 'initial_amount', 'foreign_hedging',
            'transaction_confirmation', 'empty_kyc_form_path', 'investor_profile_path',
            'myway_module_path', 'ntac', 'reporting_loss', 'share_focus',
            'date_of_alignment', 'end_date_alignment', 'type_of_business_settlement',
            'special_conditions', 'discount_applied', 'discount_amount_percent',
            'flat_fee_applied', 'flat_fee_percent', 'invested_assets', 'income_pa',
            'current_return_on_assets', 'target_roa', 'net_new_money_potential',
            'business_case_communication', 'fee_model', 'mandate_fee',
            'service_and_execution', 'no_discount', 'no_discount_amount_percent',
            'no_flat_fee', 'no_flat_fee_amount', 'transaction_fee',
            'standard_fee_discount', 'shares_fee', 'shares_fee_amount',
            'shares_discount', 'shares_discount_amount', 'investment_funds_fee',
            'investment_fund_fee_amount', 'investment_fund_discount',
            'investment_fund_discount_amount', 'fixed_income_fee',
            'fixed_income_fee_amount', 'fixed_income_discount',
            'fixed_income_discount_amount', 'fixed_income_investment_funds_fee',
            'fixed_income_investment_funds_fee_amount', 'fixed_income_investment_funds_discount',
            'fixed_income_investment_funds_discount_amount', 'shares_investment_funds_fee',
            'shares_investment_funds_fee_amount', 'shares_investment_funds_discount',
            'shares_investment_funds_discount_amount', 'status'
        ],
        'list_display': ['portfolio_name', 'portfolio_id', 'investment_amount', 'reference_currency', 'status'],
        'filter_fields': ['status', 'reference_currency', 'investment_service'],
    })

    CrudRegistry.register(LE_Account, {
        'section': 'le',
        'fields': ['id', 'client_uuid', 'product_uuid', 'product_info', 'reference_currency', 'created_at'],
        'list_display': ['product_info', 'reference_currency'],
        'filter_fields': ['client_uuid', 'product_uuid', 'reference_currency'],
        'search_fields': ['reference_currency'],
    })

    CrudRegistry.register(LE_ClientAdvisor, {
        'section': 'le',
        'fields': ['id', 'client_uuid', 'first_name', 'last_name', 'first_and_last_name', 'email', 'desk', 'branch', 'role'],
        'list_display': ['last_name', 'first_name', 'role', 'branch'],
        'filter_fields': ['role', 'branch'],
    })

    CrudRegistry.register(LE_MeetingPreparation, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'place', 'date_of_meeting', 'time',
            'hospitality', 'performance_since_beginning'
        ],
        'list_display': ['date_of_meeting', 'time', 'place', 'hospitality'],
    })
