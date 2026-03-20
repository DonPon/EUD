import uuid
from django.db import models
from apps.core.models import ClientRelatedModel

class BankingRelationship(ClientRelatedModel):
    """The Hub for the Star Schema architecture."""
    TYPE_OF_ACCOUNT_CHOICES = [
        ('120', '120'),
        ('131', '131'),
        ('132', '132'),
    ]
    SIGNATURE_CHOICES = [
        ('Joint', 'Joint'),
        ('Disjoint', 'Disjoint'),
    ]
    CLIENT_SEGMENT_CHOICES = [
        ('CORA', 'CORA'),
        ('HNWI', 'HNWI'),
    ]
    CODE_KSC_CHOICES = [
        ('541', '541'),
        ('543', '543'),
        ('546', '546'),
        ('548', '548'),
        ('561', '561'),
        ('563', '563'),
        ('566', '566'),
        ('568', '568'),
    ]
    LANGUAGE_CHOICES = [
        ('German', 'German'),
        ('English', 'English'),
        ('Spanish', 'Spanish'),
    ]
    AGREEMENT_FEES_CHOICES = [
        ('Normal case', 'Normal case'),
        ('Complete payout', 'Complete payout'),
        ('Partial payout', 'Partial payout'),
    ]

    STATUS_CHOICES = [
        ('pending_review', 'Pending Review'),
        ('review_completed', 'Review Completed'),
        ('ready_for_bot_1', 'Ready for Bot 1'),
        ('ready_for_bot_2', 'Ready for Bot 2'),
        ('ready_for_bot_3', 'Ready for Bot 3'),
        ('ready_for_bot_4', 'Ready for Bot 4'),
        ('ready_for_bot_5', 'Ready for Bot 5'),
        ('ready_for_bot_6', 'Ready for Bot 6'),
        ('ready_for_bot_7', 'Ready for Bot 7'),
        ('ready_for_bot_8', 'Ready for Bot 8'),
        ('completed', 'Completed'),
    ]

    banking_relationship = models.CharField(max_length=255, blank=True)
    technical_account = models.BooleanField(default=False)
    additional_br = models.CharField(max_length=255, blank=True)
    distribution_list = models.CharField(max_length=255, blank=True)
    name_of_banking_relationship = models.CharField(max_length=255, blank=True)
    type_of_account = models.CharField(max_length=50, choices=TYPE_OF_ACCOUNT_CHOICES, blank=True)
    type_of_signature = models.CharField(max_length=50, choices=SIGNATURE_CHOICES, blank=True)
    client_segment = models.CharField(max_length=50, choices=CLIENT_SEGMENT_CHOICES, blank=True)
    code_ksc = models.CharField(max_length=50, choices=CODE_KSC_CHOICES, blank=True)
    recording_phone_calls = models.BooleanField(default=False)
    declaration_email = models.EmailField(blank=True, null=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, blank=True)
    opened_in_ubs_premises = models.BooleanField(default=False)
    instructions = models.TextField(blank=True)
    status = models.JSONField(default=list, blank=True)
    
    # JSON Fields for multi-select
    account_and_securities_statements = models.JSONField(default=list, blank=True)
    type_and_purpose = models.JSONField(default=list, blank=True)
    agreement_distribution_fees = models.CharField(max_length=100, choices=AGREEMENT_FEES_CHOICES, blank=True)
    send_documents = models.JSONField(default=list, blank=True)
    
    csc = models.CharField(max_length=255, blank=True)
    ateco = models.CharField(max_length=255, blank=True)
    sae = models.CharField(max_length=255, blank=True)
    level_of_professionalism = models.IntegerField(null=True, blank=True)
    number_of_portfolios = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.client_uuid:
            self.client_uuid = self.id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_of_banking_relationship or f"BR: {self.banking_relationship}"

class AdditionalFormDE(ClientRelatedModel):
    AMOUNT_CHOICES = [
        ('Up to an amount of (EUR)', 'Up to an amount of (EUR)'),
        ('Up to the total savers allowance', 'Up to the total savers allowance'),
        ('Over EUR 0', 'Over EUR 0'),
    ]
    TIMELINE_CHOICES = [
        ('Until 31 December', 'Until 31 December'),
        ('As long as you have received another amount', 'As long as you have received another amount'),
        ('This order is valid as of', 'This order is valid as of'),
        ('Or from the start of the business relationship', 'Or from the start of the business relationship'),
    ]
    EXECUTION_CHOICES = [
        ('Weekly', 'Weekly'),
        ('Every 2 weeks', 'Every 2 weeks'),
        ('Monthly', 'Monthly'),
        ('Every 2 months', 'Every 2 months'),
        ('Every 3 months', 'Every 3 months'),
        ('Every 4 months', 'Every 4 months'),
        ('Every 6 months', 'Every 6 months'),
        ('Annually', 'Annually'),
    ]

    request_to_become_professional = models.BooleanField(default=False)
    forward_trading_transactions = models.BooleanField(default=False)
    exemption_order = models.BooleanField(default=False)
    last_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    name_at_birth = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    no = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    identification_number = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=100, choices=AMOUNT_CHOICES, blank=True)
    timeline = models.CharField(max_length=100, choices=TIMELINE_CHOICES, blank=True)
    date_until = models.DateField(null=True, blank=True)
    valid_as_of = models.DateField(null=True, blank=True)
    standing_order_form = models.BooleanField(default=False)
    execution = models.CharField(max_length=100, choices=EXECUTION_CHOICES, blank=True)
    day_of_execution = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    until_canceled = models.BooleanField(default=False)
    limited_power_of_attorney = models.BooleanField(default=False)
    poa_all_accounts = models.BooleanField(default=False)
    poa_in_case_of_death = models.BooleanField(default=False)
    tax_at_source_canada = models.BooleanField(default=False)
    ubs_digital_banking_authorization = models.BooleanField(default=False)

class PersonalInformation(ClientRelatedModel):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    first_and_last_name = models.CharField(max_length=255, blank=True)
    name_at_birth = models.CharField(max_length=255, blank=True)
    federal_state = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True)
    country_of_birth = models.CharField(max_length=255, blank=True)
    marital_status = models.CharField(max_length=100, blank=True)
    occupation_sector = models.CharField(max_length=255, blank=True)
    fiscal_identifier = models.CharField(max_length=255, blank=True)
    indication_tin = models.CharField(max_length=255, blank=True)
    sensitive_client = models.BooleanField(default=False)

class Address(ClientRelatedModel):
    TYPE_CHOICES = [
        ('Domicile', 'Domicile'),
        ('Correspondence', 'Correspondence'),
        ('Third party', 'Third party'),
        ('Tax domicile', 'Tax domicile'),
        ('Fiscal residence', 'Fiscal residence'),
    ]
    person_entity = models.CharField(max_length=255, blank=True)
    type_of_address = models.CharField(max_length=100, choices=TYPE_CHOICES, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    c_o = models.CharField(max_length=255, blank=True, verbose_name="C/O")
    street = models.CharField(max_length=255, blank=True)
    no = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    documents_sent = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"

class Communication(ClientRelatedModel):
    PHONE_CHOICES = [('Work', 'Work'), ('Private', 'Private')]
    MOBILE_CHOICES = [('Work', 'Work'), ('Private', 'Private')]
    EMAIL_CHOICES = [('Work', 'Work'), ('Private', 'Private')]
    FAX_CHOICES = [('Work', 'Work'), ('Private', 'Private')]

    first_and_last_name = models.CharField(max_length=255, blank=True)
    landline = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, choices=PHONE_CHOICES, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    mobile_work = models.CharField(max_length=20, choices=MOBILE_CHOICES, blank=True)
    mobile_number = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=20, choices=EMAIL_CHOICES, blank=True)
    email_address = models.EmailField(blank=True, null=True)
    fax = models.CharField(max_length=20, choices=FAX_CHOICES, blank=True)
    fax_address = models.CharField(max_length=255, blank=True)
    pec_address = models.EmailField(blank=True, null=True)

class ClientAdvisor(ClientRelatedModel):
    ROLE_CHOICES = [
        ('Requestor', 'Requestor'),
        ('Client Advisor', 'Client Advisor'),
        ('Deputy Client Advisor', 'Deputy Client Advisor'),
    ]
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    first_and_last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True, null=True)
    desk = models.CharField(max_length=255, blank=True)
    branch = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, blank=True)

class Nationality(ClientRelatedModel):
    is_main_nationality = models.BooleanField(default=False)
    nationality = models.CharField(max_length=255, blank=True)
    nci = models.CharField(max_length=255, blank=True)
    id_type = models.CharField(max_length=255, blank=True)
    fiscal_code = models.CharField(max_length=255, blank=True)
    fiscal_code_path = models.CharField(max_length=255, blank=True)
    release_authority = models.CharField(max_length=255, blank=True)
    release_location = models.CharField(max_length=255, blank=True)
    release_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    is_id_document_provided = models.BooleanField(default=False)
    id_document_path = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Nationalities"

class TIN(ClientRelatedModel):
    aei_tin = models.CharField(max_length=255, blank=True, verbose_name="AEI/TIN")

    class Meta:
        verbose_name = "TIN"
        verbose_name_plural = "TINs"

class EBanking(ClientRelatedModel):
    has_ebanking = models.BooleanField(default=False)
    contract_number = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "E-Banking"
        verbose_name_plural = "E-Banking"

class MeetingPreparation(ClientRelatedModel):
    PLACE_CHOICES = [('Internal', 'Internal'), ('External', 'External')]
    HOSPITALITY_CHOICES = [
        ('None', 'None'),
        ('Cold drinks, coffee or tea on request', 'Cold drinks, coffee or tea on request'),
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
    ]
    place = models.CharField(max_length=50, choices=PLACE_CHOICES, blank=True)
    number_of_participants = models.IntegerField(null=True, blank=True)
    date_of_meeting = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    room_booking = models.BooleanField(default=False)
    hospitality = models.CharField(max_length=100, choices=HOSPITALITY_CHOICES, blank=True)
    technical_equipment_needed = models.BooleanField(default=False)
    performance_since_beginning = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    performance_before_tax = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    performance_since_start = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    investor_profile_link = models.URLField(blank=True, null=True)
    email_waiver = models.BooleanField(default=False)

class Relationship(ClientRelatedModel):
    """The Edge Table / Graph."""
    child_unique_id = models.UUIDField(db_index=True)
    type_of_relationship = models.CharField(max_length=255, blank=True)
    type_of_access = models.CharField(max_length=255, blank=True)
    level_of_access = models.JSONField(default=list, blank=True)
    relation_with_owner = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Relation: {self.client_uuid} -> {self.child_unique_id}"

class Product(ClientRelatedModel):
    # Choices
    FOREIGN_HEDGING_CHOICES = [
        ('Discretion of UBS', 'Discretion of UBS'),
        ('None for share allocation', 'None for share allocation'),
    ]
    NTAC_CHOICES = [
        ('Excluded', 'Excluded'),
        ('Permitted', 'Permitted'),
    ]
    REPORTING_LOSS_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
    ]
    SHARE_FOCUS_CHOICES = [
        ('EMU: Predominantly...', 'EMU: Predominantly...'),
        ('Global equity...', 'Global equity...'),
    ]
    TYPE_OF_BUSINESS_SETTLEMENT_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Individual', 'Individual'),
    ]
    BUSINESS_CASE_COMMUNICATION_CHOICES = [
        ('Option 1 (in person)', 'Option 1 (in person)'),
        ('Option 2 (online)', 'Option 2 (online)'),
    ]
    FEE_MODEL_CHOICES = [
        ('Advice plus transaction fee', 'Advice plus transaction fee'),
        # Add more if needed
    ]
    SERVICE_AND_EXECUTION_CHOICES = [
        ('UBS Manage', 'UBS Manage'),
        ('UBS Advice', 'UBS Advice'),
        # Add more if needed
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_id = models.CharField(max_length=255, blank=True)
    portfolio_name = models.CharField(max_length=255, blank=True)
    email_waiver = models.BooleanField(default=False)
    reference_currency = models.CharField(max_length=10, blank=True)
    investment_service = models.CharField(max_length=255, blank=True)
    a_s_authorization_path = models.CharField(max_length=255, blank=True)
    investment_strategy = models.CharField(max_length=255, blank=True)
    ip_risk_tolerance = models.CharField(max_length=255, blank=True)
    investment_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    selected_service = models.CharField(max_length=255, blank=True)
    all_in = models.BooleanField(default=False)
    sustainable_investing = models.BooleanField(default=False)
    sustainability_preference = models.CharField(max_length=255, blank=True)
    focus_equity = models.BooleanField(default=False)
    alternative_investment = models.BooleanField(default=False)
    direct_instrument = models.BooleanField(default=False)
    initial_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    foreign_hedging = models.CharField(max_length=100, choices=FOREIGN_HEDGING_CHOICES, blank=True)
    transaction_confirmation = models.BooleanField(default=False)
    empty_kyc_form_path = models.CharField(max_length=255, blank=True)
    investor_profile_path = models.CharField(max_length=255, blank=True)
    myway_module_path = models.CharField(max_length=255, blank=True)
    ntac = models.CharField(max_length=50, choices=NTAC_CHOICES, blank=True)
    reporting_loss = models.CharField(max_length=50, choices=REPORTING_LOSS_CHOICES, blank=True)
    share_focus = models.CharField(max_length=255, choices=SHARE_FOCUS_CHOICES, blank=True)
    date_of_alignment = models.DateField(null=True, blank=True)
    end_date_alignment = models.DateField(null=True, blank=True)
    type_of_business_settlement = models.CharField(max_length=50, choices=TYPE_OF_BUSINESS_SETTLEMENT_CHOICES, blank=True)
    special_conditions = models.TextField(blank=True)
    discount_applied = models.BooleanField(default=False)
    discount_amount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    flat_fee_applied = models.BooleanField(default=False)
    flat_fee_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    invested_assets = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    income_pa = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    current_return_on_assets = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    target_roa = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    net_new_money_potential = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    business_case_communication = models.TextField(choices=BUSINESS_CASE_COMMUNICATION_CHOICES, blank=True)
    fee_model = models.CharField(max_length=255, blank=True)
    mandate_fee = models.BooleanField(default=False)
    service_and_execution = models.CharField(max_length=255, blank=True)
    no_discount = models.BooleanField(default=False)
    no_discount_amount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_flat_fee = models.BooleanField(default=False)
    no_flat_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    transaction_fee = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    standard_fee_discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    shares_fee = models.BooleanField(default=False)
    shares_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    shares_discount = models.BooleanField(default=False)
    shares_discount_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    investment_funds_fee = models.BooleanField(default=False)
    investment_fund_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    investment_fund_discount = models.BooleanField(default=False)
    investment_fund_discount_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fixed_income_fee = models.BooleanField(default=False)
    fixed_income_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fixed_income_discount = models.BooleanField(default=False)
    fixed_income_discount_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fixed_income_investment_funds_fee = models.BooleanField(default=False)
    fixed_income_investment_funds_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fixed_income_investment_funds_discount = models.BooleanField(default=False)
    fixed_income_investment_funds_discount_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    shares_investment_funds_fee = models.BooleanField(default=False)
    shares_investment_funds_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    shares_investment_funds_discount = models.BooleanField(default=False)
    shares_investment_funds_discount_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.portfolio_name} ({self.portfolio_id})"

class Account(ClientRelatedModel):
    product_uuid = models.UUIDField(db_index=True, null=True, blank=True)
    reference_currency = models.CharField(max_length=3, default='USD')

    @property
    def product_info(self):
        """Virtual field to show product details in tables without a hard FK."""
        try:
            from .models import Product
            p = Product.objects.get(id=self.product_uuid)
            return f"{p.portfolio_name} ({p.portfolio_id})"
        except:
            return "N/A"
