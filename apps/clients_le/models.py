import uuid
from django.db import models
from apps.core.models import ClientRelatedModel

class LE_BankingRelationship(ClientRelatedModel):
    """The Hub for Legal Entity Clients (Star Schema)."""
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

    legal_name = models.CharField(max_length=255, blank=True)
    banking_relationship = models.CharField(max_length=255, blank=True)
    technical_account = models.BooleanField(default=False)
    client_segment = models.CharField(max_length=50, blank=True)
    code_ksc = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, blank=True)
    status = models.JSONField(default=list, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.client_uuid:
            self.client_uuid = self.id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.legal_name or f"LE BR: {self.banking_relationship}"

    class Meta:
        verbose_name = "LE Banking Relationship"
        verbose_name_plural = "LE Banking Relationships"

class LE_Information(ClientRelatedModel):
    """Detailed information for Legal Entities."""
    LEGAL_FORM_CHOICES = [
        ('AG', 'Aktiengesellschaft (AG)'),
        ('GmbH', 'Gesellschaft mit beschränkter Haftung (GmbH)'),
        ('Foundation', 'Foundation'),
        ('Trust', 'Trust'),
        ('Other', 'Other'),
    ]
    
    legal_name = models.CharField(max_length=255, blank=True)
    legal_form = models.CharField(max_length=100, choices=LEGAL_FORM_CHOICES, blank=True)
    registration_number = models.CharField(max_length=100, blank=True)
    country_of_registration = models.CharField(max_length=100, blank=True)
    date_of_registration = models.DateField(null=True, blank=True)
    tax_id = models.CharField(max_length=100, blank=True, verbose_name="Tax ID / VAT")
    lei_code = models.CharField(max_length=100, blank=True, verbose_name="LEI Code")
    industry_sector = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "LE Information"
        verbose_name_plural = "LE Information"

class LE_Address(ClientRelatedModel):
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
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

class LE_Communication(ClientRelatedModel):
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

    class Meta:
        verbose_name = "Communication"
        verbose_name_plural = "Communications"

class LE_ClientAdvisor(ClientRelatedModel):
    ROLE_CHOICES = [
        ('Requestor', 'Requestor'),
        ('Client Advisor', 'Client Advisor'),
        ('Deputy Client Advisor', 'Deputy Client Advisor'),
    ]
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True, null=True)
    desk = models.CharField(max_length=255, blank=True)
    branch = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, blank=True)

    class Meta:
        verbose_name = "Client Advisor"
        verbose_name_plural = "Client Advisors"

class LE_Nationality(ClientRelatedModel):
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
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"

class LE_TIN(ClientRelatedModel):
    aei_tin = models.CharField(max_length=255, blank=True, verbose_name="AEI/TIN")

    class Meta:
        verbose_name = "TIN"
        verbose_name_plural = "TINs"

class LE_EBanking(ClientRelatedModel):
    has_ebanking = models.BooleanField(default=False)
    contract_number = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "EBanking"
        verbose_name_plural = "EBanking"

class LE_MeetingPreparation(ClientRelatedModel):
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

    class Meta:
        verbose_name = "Meeting Preparation"
        verbose_name_plural = "Meeting Preparations"

class LE_Relationship(ClientRelatedModel):
    """The Edge Table / Graph."""
    child_unique_id = models.UUIDField(db_index=True)
    type_of_relationship = models.CharField(max_length=255, blank=True)
    type_of_access = models.CharField(max_length=255, blank=True)
    level_of_access = models.JSONField(default=list, blank=True)
    relation_with_owner = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Relation: {self.client_uuid} -> {self.child_unique_id}"

    class Meta:
        verbose_name = "Relationship"
        verbose_name_plural = "Relationships"

class LE_Product(ClientRelatedModel):
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

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class LE_Account(ClientRelatedModel):
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
    
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"