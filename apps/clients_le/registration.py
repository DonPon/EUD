from apps.generic_crud.registry import CrudRegistry
from .models import LE_TIN, LE_AdditionalFormDE, LE_Account, LE_BankingRelationship, LE_ClientAdvisor, LE_Company, LE_EBanking, LE_Address, LE_Communication, LE_MeetingPreparation, LE_Nationality, LE_PersonalInformation, LE_Product, LE_Relationship

def register_le_clients_models():
    """Register all Legal Entity models for generic CRUD."""
    
    CrudRegistry.register(LE_BankingRelationship, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'name_of_banking_relationship', 'banking_relationship',
            'additional_br', 'partner_id', 'type_of_account', 'type_of_signature',
            'segment_type', 'client_segment', 'code_csc', 'communication_br',
            'third_postal_address', 'beneficial_owner', 'id_doc_provided',
            'language', 'opened_in_ubs_premises', 'account_and_securities_statements',
            'type_and_purpose', 'type_and_purpose_specify', 'reporting_obligation',
            'br_client_type', 'earning_statements', 'earning_statements_fees',
            'fiscal_identifier', 'agreement_distribution_fees', 'agreement_percentage',
            'number_of_portfolios', 'delivery_date', 'time', 'document_format',
            'distance_mode', 'ateco', 'sae', 'level_of_professionalism',
            'send_documents', 'further_notes', 'status', 'created_at'
        ],
        'list_display': ['name_of_banking_relationship', 'banking_relationship', 'client_segment', 'status'],
        'filter_fields': ['client_segment', 'code_csc', 'language', 'type_and_purpose', 'reporting_obligation'],
        'search_fields': ['name_of_banking_relationship', 'banking_relationship'],
    })

    CrudRegistry.register(LE_Company, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'type_of_company', 'name_of_company', 'ivacf', 'iva',
            'lei_code', 'date_of_constitution', 'place_of_constitution',
            'country_of_constitution', 'fiscal_residence', 'cciaa_type', 'cciaa_number',
            'released_by', 'date_of_issue', 'form_of_legal_entity',
            'level_of_professionalism', 'ateco', 'sae', 'id_third_account_owner',
            'last_name_tao', 'first_name_tao', 'street_tao', 'no_tao',
            'postal_code_tao', 'city_tao', 'country_tao', 'created_at'
        ],
        'list_display': ['name_of_company', 'type_of_company', 'lei_code', 'fiscal_residence'],
        'filter_fields': ['type_of_company', 'fiscal_residence', 'form_of_legal_entity'],
        'search_fields': ['name_of_company', 'lei_code'],
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
            'id', 'client_uuid', 'first_and_last_name', 'type_of_address',
            'c_o', 'street', 'no', 'postal_code', 'city', 'province', 'country',
            'annual_tax_cert', 'receive_copies_of_original', 'third_party_copies'
        ],
        'list_display': ['first_and_last_name', 'type_of_address', 'city', 'country'],
        'filter_fields': ['type_of_address', 'country'],
        'search_fields': ['city', 'street', 'first_and_last_name'],
    })

    CrudRegistry.register(LE_TIN, {
        'section': 'le',
        'fields': ['id', 'client_uuid', 'aei_tin'],
        'list_display': ['aei_tin'],
    })

    CrudRegistry.register(LE_Communication, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'first_and_last_name', 'type_of_comunication',
            'comunication_Context', 'prefix', 'number', 'address'
        ],
        'list_display': ['first_and_last_name', 'type_of_comunication', 'address'],
        'search_fields': ['first_and_last_name', 'address'],
    })

    CrudRegistry.register(LE_EBanking, {
        'section': 'le',
        'fields': ['id', 'client_uuid', 'has_ebanking', 'first_and_last_name', 'first_name', 'last_name', 'access_type', 'contract_number'],
        'list_display': ['has_ebanking', 'first_and_last_name', 'first_name', 'last_name', 'contract_number'],
    })

    CrudRegistry.register(LE_Relationship, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'child_unique_id', #'first_and_last_name',
            'tax_domicile', 'technical_account', 'type_of_relationship', 'full_name', 'relationship_with_owner', 
            'role', 'lr_executor', 'lr_beneficial_owner', 'lr_bo_role'
        ],
        'list_display': [
            #'related_banking_relationship',
            #'related_name_of_banking_relationship',
            #'related_first_name',
            #'related_last_name',
            'full_name',
            'type_of_relationship',
            'relationship_with_owner',
            'related_client_link'
        ],
        'filter_fields': ['type_of_relationship', 'tax_domicile'],
    })

    CrudRegistry.register(LE_Product, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'portfolio_id', 'portfolio_name', 'email_waiver',
            'reference_currency', 'investment_strategy', 'ip_risk_tolerance',
            'investment_service', 'investment_amount', 'selected_service',
            'all_in', 'sustainable_investing', 'sustainability_preference',
            'focus_equity', 'alternative_investment', 'direct_instrument',
            'initial_amount', 'currency_hedging', 'transaction_confirmation',
            'white_KYC_provided', 'fiduciary_mandate_provided', 'fiscal_regime',
            'ntac', 'reporting_loss', 'share_focus', 'hedging_foreign_currency',
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
        'fields': ['id', 'client_uuid', 'role_client_advisor', 'first_and_last_name', 'first_name', 'last_name', 'email', 'branch', 'desk', 'distribution_list'],
        'list_display': ['last_name', 'first_name', 'role_client_advisor', 'branch', 'desk'],
        'filter_fields': ['role_client_advisor', 'branch'],
    })

    CrudRegistry.register(LE_MeetingPreparation, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'place', 'date_of_meeting', 'time',
            'number_of_participants', 'room_booking', 'hospitality',
            'technical_equipment_needed', 'parking_space_client', 'pool_car',
            'from_date', 'from_time', 'to_date', 'to_time', 'planned_contact',
            'contact_CST', 'stored_reporting_t2_ptf', 'performance_since_beginning',
            'performance_before_tax', 'performance_since_start', 'health_check',
            'Remarks_documents', 'investor_profile_link', 'email_waiver'
        ],
        'list_display': ['date_of_meeting', 'time', 'place', 'hospitality'],
    })


    CrudRegistry.register(LE_AdditionalFormDE, {
        'section': 'le',
        'fields': [
            'id', 'client_uuid', 'forward_trading_transactions', 'exemption_order',
            'last_name', 'first_name', 'name_at_birth', 'street', 'no',
            'postal_code', 'city', 'country', 'identification_number',
            'date_of_birth', 'amount', 'timeline', 'date_until', 'valid_as_of',
            'standing_order_form', 'execution', 'day_of_execution',
            'first_time_execution', 'month', 'year', 'validity',
            'valid_until_date', 'tax_at_source_canada', 'transfer_another_bank'
        ],
        'list_display': ['last_name', 'first_name', 'identification_number', 'amount'],
        'filter_fields': ['amount', 'execution'],
    })