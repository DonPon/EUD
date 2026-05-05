from apps.generic_crud.registry import CrudRegistry
from .models import (
    BankingRelationship, AdditionalFormDE, PersonalInformation, Address,
    Communication, ClientAdvisor, Nationality, TIN, EBanking,
    Product, MeetingPreparation, Relationship, Account
)

def register_clients_models():
    """Register all Bank Client models for generic CRUD."""
    
    CrudRegistry.register(BankingRelationship, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'name_of_banking_relationship', 'banking_relationship',
            'additional_br', 'partner_id', 'type_of_account', 'type_of_signature',
            'segment_type', 'client_segment', 'code_ksc', 'communication_br',
            'third_postal_address', 'beneficial_owner', 'id_doc_provided', 'language',
            'opened_in_ubs_premises', 'account_and_securities_statements',
            'type_and_purpose', 'type_and_purpose_specify', 'reporting_obligation',
            'br_client_type', 'earning_statements', 'earning_statements_fees',
            'fiscal_identifier', 'agreement_distribution_fees', 'agreement_percentage',
            'number_of_portfolios', 'delivery_date', 'time', 'document_format',
            'distance_mode', 'ateco', 'sae', 'level_of_professionalism',
            'send_documents', 'further_notes', 'status', 'created_at'
        ],
        'list_display': ['name_of_banking_relationship', 'banking_relationship', 'type_of_account', 'client_segment', 'status'],
        'filter_fields': ['type_of_account', 'client_segment', 'code_ksc', 'language', 'br_client_type'],
        'search_fields': ['name_of_banking_relationship', 'banking_relationship', 'partner_id'],
    })

    CrudRegistry.register(PersonalInformation, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'technical_account', 'type_of_relationship',
            'first_and_last_name', 'first_name', 'last_name', 'name_at_birth',
            'type_id_NCI', 'fiscal_it_number', 'type_id_document', 'release_authority',
            'release_place', 'release_date', 'expiry_date', 'copy_id_provided',
            'place_of_birth', 'date_of_birth', 'country_of_birth', 'marital_status',
            'occupation_sector', 'fiscal_identifier', 'fiscal_residence',
            'has_ebanking', 'sensitive_client'
        ],
        'list_display': ['first_name', 'last_name', 'type_of_relationship', 'date_of_birth', 'marital_status'],
        'filter_fields': ['type_of_relationship', 'marital_status', 'sensitive_client'],
        'search_fields': ['first_name', 'last_name', 'first_and_last_name', 'fiscal_identifier', 'fiscal_it_number'],
    })

    CrudRegistry.register(Nationality, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'is_main_nationality', 'nationality', 'nci', 'id_type',
            'fiscal_code', 'release_authority', 'release_date', 'expiry_date'
        ],
        'list_display': ['nationality', 'is_main_nationality', 'id_type', 'expiry_date'],
        'filter_fields': ['is_main_nationality', 'id_type'],
    })

    CrudRegistry.register(Address, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'first_and_last_name', 'type_of_address', 'c_o',
            'street', 'no', 'postal_code', 'city', 'province', 'country',
            'annual_tax_cert', 'receive_copies_of_original', 'third_party_copies'
        ],
        'list_display': ['type_of_address', 'city', 'country', 'first_and_last_name'],
        'filter_fields': ['type_of_address', 'country', 'annual_tax_cert'],
        'search_fields': ['city', 'street', 'first_and_last_name'],
    })

    CrudRegistry.register(TIN, {
        'section': 'np',
        'fields': ['id', 'client_uuid', 'aei_tin'],
        'list_display': ['aei_tin'],
    })

    CrudRegistry.register(Communication, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'first_and_last_name', 'type_of_communication',
            'communication_context', 'prefix', 'number', 'address'
        ],
        'list_display': ['first_and_last_name', 'type_of_communication', 'number'],
        'search_fields': ['first_and_last_name', 'number'],
    })

    CrudRegistry.register(EBanking, {
        'section': 'np',
        'fields': ['id', 'client_uuid', 'first_name', 'last_name', 'access_type', 'contract_number'],
        'list_display': ['first_name', 'last_name', 'contract_number'],
    })

    CrudRegistry.register(Relationship, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'child_unique_id', #'first_and_last_name',
            'tax_domicile', 'technical_account', 'type_of_relationship', 'full_name', 'relationship_with_owner'
        ],
        'list_display': [
            'related_banking_relationship',
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

    CrudRegistry.register(Product, {
        'section': 'np',
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

    CrudRegistry.register(Account, {
        'section': 'np',
        'fields': ['id', 'client_uuid', 'product_uuid', 'product_info', 'reference_currency', 'created_at'],
        'list_display': ['product_info', 'reference_currency'],
        'filter_fields': ['client_uuid', 'product_uuid', 'reference_currency'],
        'search_fields': ['reference_currency'],
    })

    CrudRegistry.register(ClientAdvisor, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'role_client_advisor', 'first_and_last_name',
            'first_name', 'last_name', 'email', 'branch', 'distribution_list'
        ],
        'list_display': ['role_client_advisor', 'first_and_last_name', 'branch'],
        'filter_fields': ['role_client_advisor', 'branch'],
    })

    CrudRegistry.register(MeetingPreparation, {
        'section': 'np',
        'fields': [
            'id', 'client_uuid', 'place', 'date_of_meeting', 'time',
            'number_of_participants', 'room_booking', 'hospitality',
            'technical_equipment_needed', 'parking_space_client', 'pool_car',
            'from_date', 'from_time', 'to_date', 'to_time',
            'planned_contact', 'contact_CST', 'stored_reporting_t2_ptf',
            'performance_since_beginning', 'performance_before_tax',
            'performance_since_start', 'health_check', 'remarks_documents',
            'investor_profile_link', 'email_waiver'
        ],
        'list_display': ['date_of_meeting', 'time', 'place', 'hospitality'],
    })

    CrudRegistry.register(AdditionalFormDE, {
        'section': 'np',
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
