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

    TYPE_OF_ACCOUNT_CHOICES = [
        ('Individual', 'Individual'),
        ('Joint', 'Joint'),
    ]
    SIGNATURE_CHOICES = [
        ('Single', 'Single'),
        ('Joint', 'Joint'),
    ]
    SEGMENT_TYPE_CHOICES = [
        ('120', '120'),
        ('132', '132'),
        ('131', '131'),
    ]

    COMMUNICATION_BR_CHOICES = [
        ('Phone', 'Phone'),
        ('Email', 'Email'),
    ]
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    BENEFICIAL_OWNER_CHOICES = [
        ('Same as owner', 'Same as owner'),
        ('Third party', 'Third party'),
    ]
    ID_DOC_PROVIDED_CHOICES = [
        ('Provided', 'Provided'),
        ('Not provided', 'Not provided'),
    ]
    LANGUAGE_CHOICES = [
        ('German', 'German'),
        ('English', 'English'),
        ('Italian', 'Italian'),
        ('Spanish', 'Spanish'),
    ]
    OPENED_IN_UBS_PREMISES_CHOICES = [
        ('Inside premises', 'Inside premises'),
        ('Outside premises', 'Outside premises'),
    ]
    ACCOUNT_STATEMENTS_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Daily', 'Daily'),
    ]
    TYPE_AND_PURPOSE_CHOICES = [
        ('Payment', 'Payment'),
        ('Investment', 'Investment'),
    ]
    REPORTING_OBLIGATION_CHOICES = [
        ('Reported by UBS', 'Reported by UBS'),
        ('Reported by Client', 'Reported by Client'),
    ]
    BR_CLIENT_TYPE_CHOICES = [
        ('Private', 'Private'),
        ('Business', 'Business'),
    ]
    AGREEMENT_FEES_CHOICES = [
        ('Normal', 'Normal'),
        ('Complete', 'Complete'),
        ('Partial', 'Partial'),
    ]
    NUMBER_OF_PORTFOLIOS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    SEND_DOCUMENTS_CHOICES = [
        ('To client', 'To client'),
        ('To CA', 'To CA'),
        ('Digitally', 'Digitally'),
    ]

    name_of_banking_relationship = models.CharField(max_length=255, null=True, blank=True, verbose_name="Name Banking Relationship")
    banking_relationship = models.CharField(max_length=255, null=True, blank=True, verbose_name="Banking Relationship")
    additional_br = models.CharField(max_length=255, null=True, blank=True, verbose_name="Additional Banking Relationship")
    partner_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="Partner ID")
    type_of_account = models.CharField(max_length=50, choices=TYPE_OF_ACCOUNT_CHOICES, blank=True, null=True, verbose_name="Type of Account")
    type_of_signature = models.CharField(max_length=50, choices=SIGNATURE_CHOICES, blank=True, null=True, verbose_name="Type of Signature")
    segment_type = models.CharField(max_length=10, choices=SEGMENT_TYPE_CHOICES, null=True, blank=True)
    client_segment = models.CharField(max_length=255, null=True, blank=True, verbose_name="Client Segment")
    code_csc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Client Segment Code (CSC)")
    communication_br = models.CharField(max_length=50, choices=COMMUNICATION_BR_CHOICES, blank=True, null=True, verbose_name="Communication mode")
    third_postal_address = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Third Postal Address")
    beneficial_owner = models.CharField(max_length=50, choices=BENEFICIAL_OWNER_CHOICES, blank=True, null=True, verbose_name="Beneficial Owner")
    id_doc_provided = models.CharField(max_length=50, choices=ID_DOC_PROVIDED_CHOICES, blank=True, null=True, verbose_name="ID copy provided")
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, blank=True, null=True, verbose_name="Language")
    opened_in_ubs_premises = models.CharField(max_length=50, choices=OPENED_IN_UBS_PREMISES_CHOICES, blank=True, null=True, verbose_name="Account Opening Location")
    account_and_securities_statements = models.CharField(max_length=100, choices=ACCOUNT_STATEMENTS_CHOICES, blank=True, null=True, verbose_name="transaction statements")
    type_and_purpose = models.CharField(max_length=100, choices=TYPE_AND_PURPOSE_CHOICES, blank=True, null=True, verbose_name="Purpose of Banking Relations")
    type_and_purpose_specify = models.CharField(max_length=255, null=True, blank=True, verbose_name="Details of Purpose")
    reporting_obligation = models.CharField(max_length=50, choices=REPORTING_OBLIGATION_CHOICES, blank=True, null=True, verbose_name="Reporting Accordance")
    br_client_type = models.CharField(max_length=50, choices=BR_CLIENT_TYPE_CHOICES, blank=True, null=True, verbose_name="Client Type")
    earning_statements = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Earnings Statements")
    earning_statements_fees = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Fees")
    fiscal_identifier = models.CharField(max_length=255, null=True, blank=True, verbose_name="Fiscal Identifier")
    agreement_distribution_fees = models.CharField(max_length=100, choices=AGREEMENT_FEES_CHOICES, blank=True, null=True, verbose_name="Distribution Fees Agreement")
    agreement_percentage = models.CharField(max_length=255, null=True, blank=True, verbose_name="Percentage For The Client")
    number_of_portfolios = models.IntegerField(choices=NUMBER_OF_PORTFOLIOS_CHOICES, null=True, blank=True, verbose_name="Number of Portfolios")
    delivery_date = models.DateField(null=True, blank=True, verbose_name="Delivery Date")
    time = models.TimeField(null=True, blank=True, verbose_name="Time")
    document_format = models.CharField(max_length=255, null=True, blank=True, verbose_name="Document Format")
    distance_mode = models.CharField(max_length=255, null=True, blank=True, verbose_name="Distance Mode")
    ateco = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ateco")
    sae = models.CharField(max_length=255, null=True, blank=True, verbose_name="Sae")
    level_of_professionalism = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Professional Client")
    send_documents = models.CharField(max_length=50, choices=SEND_DOCUMENTS_CHOICES, blank=True, null=True, verbose_name="Sending Documents")
    further_notes = models.TextField(null=True, blank=True, verbose_name="Notes")
    status = models.JSONField(default=list, blank=True)

    def save(self, *args, **kwargs):
        if not self.client_uuid:
            self.client_uuid = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_of_banking_relationship or f"LE BR: {self.banking_relationship}"

    class Meta:
        verbose_name = "LE Banking Relationship"
        verbose_name_plural = "LE Banking Relationships"

class LE_PersonalInformation(ClientRelatedModel):
    """Detailed information for Legal Entities."""
    LEGAL_FORM_CHOICES = [
        ('AG', 'Aktiengesellschaft (AG)'),
        ('GmbH', 'Gesellschaft mit beschränkter Haftung (GmbH)'),
        ('Foundation', 'Foundation'),
        ('Trust', 'Trust'),
        ('Other', 'Other'),
    ]

    legal_name = models.CharField(max_length=255, blank=True, null=True)
    legal_form = models.CharField(max_length=100, choices=LEGAL_FORM_CHOICES, blank=True, null=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    country_of_registration = models.CharField(max_length=100, blank=True, null=True)
    date_of_registration = models.DateField(null=True, blank=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tax ID / VAT")
    lei_code = models.CharField(max_length=100, blank=True, null=True, verbose_name="LEI Code")
    industry_sector = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    # Personal Information Fields
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_and_last_name = models.CharField(max_length=255, blank=True, null=True)
    name_at_birth = models.CharField(max_length=255, blank=True, null=True)
    federal_state = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    country_of_birth = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=100, blank=True, null=True)
    occupation_sector = models.CharField(max_length=255, blank=True, null=True)
    fiscal_identifier = models.CharField(max_length=255, blank=True, null=True)
    indication_tin = models.CharField(max_length=255, blank=True, null=True)
    sensitive_client = models.CharField(max_length=255, blank=True, null=True)
    executor = models.CharField(max_length=255, blank=True, null=True)
    beneficial_owner = models.CharField(max_length=255, blank=True, null=True)
    tef = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "LE Personal Information"
        verbose_name_plural = "LE Personal Information"

class LE_Address(ClientRelatedModel):
    TYPE_CHOICES = [
        ('Correspondence', 'Correspondence'),
        ('Domicile', 'Domicile'),
        ('Legal Address', 'Legal Address'),
    ]
    first_and_last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="full name")
    type_of_address = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, blank=True, verbose_name="address type")
    c_o = models.CharField(max_length=255, null=True, blank=True, verbose_name="c/o")
    street = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")
    no = models.CharField(max_length=50, null=True, blank=True, verbose_name="number")
    postal_code = models.CharField(max_length=50, null=True, blank=True, verbose_name="postal code")
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")
    province = models.CharField(max_length=255, null=True, blank=True, verbose_name="province")
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")
    annual_tax_cert = models.CharField(max_length=255, null=True, blank=True, verbose_name="tax certificates")
    receive_copies_of_original = models.CharField(max_length=255, null=True, blank=True, verbose_name="copy mail")
    third_party_copies = models.CharField(max_length=255, null=True, blank=True, verbose_name="third copy")

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

class LE_Communication(ClientRelatedModel):
    TYPE_CHOICES = [
        ('Telephone', 'Telephone'),
        ('Mobile', 'Mobile'),
        ('Email', 'Email'),
        ('Pec address', 'Pec address'),
        ('Fax', 'Fax'),
    ]
    CONTEXT_CHOICES = [
        ('work', 'work'),
        ('private', 'private'),
    ]

    first_and_last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="full name")
    type_of_comunication = models.CharField(max_length=255, choices=TYPE_CHOICES, null=True, blank=True, verbose_name="type")
    comunication_Context = models.CharField(max_length=255, choices=CONTEXT_CHOICES, null=True, blank=True, verbose_name="context")
    prefix = models.CharField(max_length=20, null=True, blank=True, verbose_name="prefix")
    number = models.CharField(max_length=255, null=True, blank=True, verbose_name="number")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="address")

    class Meta:
        verbose_name = "Communication"
        verbose_name_plural = "Communications"

class LE_ClientAdvisor(ClientRelatedModel):
    ROLE_CHOICES = [
        ('Requestor', 'Requestor'),
        ('Client Advisor', 'Client Advisor'),
        ('Deputy Client Advisor', 'Deputy Client Advisor'),
    ]
    role_client_advisor = models.CharField(max_length=100, choices=ROLE_CHOICES, null=True, blank=True, verbose_name="role")
    first_and_last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="full name")
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="first name")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="last name")
    email = models.EmailField(null=True, blank=True, verbose_name="email")
    branch = models.CharField(max_length=255, null=True, blank=True, verbose_name="branch")
    desk = models.CharField(max_length=255, null=True, blank=True, verbose_name="desk")
    distribution_list = models.CharField(max_length=255, null=True, blank=True, verbose_name="distribution")

    class Meta:
        verbose_name = "Client Advisor"
        verbose_name_plural = "Client Advisors"

class LE_Nationality(ClientRelatedModel):
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    is_main_nationality = models.CharField(max_length=255, blank=True, null=True, choices=YES_NO_CHOICES)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    nci = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=255, blank=True, null=True)
    fiscal_code = models.CharField(max_length=255, blank=True, null=True)
    fiscal_code_path = models.CharField(max_length=255, blank=True, null=True)
    release_authority = models.CharField(max_length=255, blank=True, null=True)
    release_location = models.CharField(max_length=255, blank=True, null=True) 
    release_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    is_id_document_provided = models.CharField(max_length=255, blank=True, null=True, choices=YES_NO_CHOICES)
    id_document_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"

class LE_TIN(ClientRelatedModel):
    aei_tin = models.CharField(max_length=255, blank=True, null=True, verbose_name="AEI/TIN")

    class Meta:
        verbose_name = "TIN"
        verbose_name_plural = "TINs"

class LE_EBanking(ClientRelatedModel):
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    has_ebanking = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="has ebanking")
    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="first and last name")
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="first name")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="last name")
    access_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="access type")
    contract_number = models.IntegerField(null=True, blank=True, verbose_name="contract")

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
    place = models.CharField(max_length=50, choices=PLACE_CHOICES, null=True, blank=True, verbose_name="place")
    date_of_meeting = models.DateField(null=True, blank=True, verbose_name="meeting date")
    time = models.TimeField(null=True, blank=True, verbose_name="time")
    number_of_participants = models.IntegerField(null=True, blank=True, verbose_name="participants")
    room_booking = models.CharField(max_length=255, null=True, blank=True, verbose_name="room booking")
    hospitality = models.CharField(max_length=100, choices=HOSPITALITY_CHOICES, null=True, blank=True, verbose_name="hospitality")
    technical_equipment_needed = models.CharField(max_length=255, null=True, blank=True, verbose_name="equipment")
    parking_space_client = models.CharField(max_length=255, null=True, blank=True, verbose_name="parking")
    pool_car = models.CharField(max_length=255, null=True, blank=True, verbose_name="pool car")
    from_date = models.DateField(null=True, blank=True, verbose_name="from date")
    from_time = models.TimeField(null=True, blank=True, verbose_name="from time")
    to_date = models.DateField(null=True, blank=True, verbose_name="to date")
    to_time = models.TimeField(null=True, blank=True, verbose_name="to time")
    planned_contact = models.CharField(max_length=255, null=True, blank=True, verbose_name="planned contact")
    contact_CST = models.CharField(max_length=255, null=True, blank=True, verbose_name="cst contact")
    stored_reporting_t2_ptf = models.CharField(max_length=255, null=True, blank=True, verbose_name="stored report")
    performance_since_beginning = models.CharField(max_length=255, null=True, blank=True, verbose_name="since begin")
    performance_before_tax = models.CharField(max_length=255, null=True, blank=True, verbose_name="before tax")
    performance_since_start = models.CharField(max_length=255, null=True, blank=True, verbose_name="since start")
    health_check = models.CharField(max_length=255, null=True, blank=True, verbose_name="health check")
    Remarks_documents = models.CharField(max_length=255, null=True, blank=True, verbose_name="remarks")
    investor_profile_link = models.CharField(max_length=255, null=True, blank=True, verbose_name="profile link")
    email_waiver = models.CharField(max_length=255, null=True, blank=True, verbose_name="email waiver")

    class Meta:
        verbose_name = "Meeting Preparation"
        verbose_name_plural = "Meeting Preparations"

class LE_Relationship(ClientRelatedModel):
    """The Edge Table / Graph."""
    TAX_DOMICILE_CHOICES = [
        ('work', 'work'),
        ('private', 'private'),
    ]
    RELATIONSHIP_CHOICES = [
        ('Owner', 'Owner'),
        ('Co-owner', 'Co-owner'),
        ('POA (for all accounts)', 'POA (for all accounts)'),
        ('POA (general)', 'POA (general)'),
        ('POA (limited)', 'POA (limited)'),
        ('POA (in case of death)', 'POA (in case of death)'),
        ('Beneficial Owner', 'Beneficial Owner'),
        ('Legal Representative', 'Legal Representative'),
    ]

    child_unique_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="child id")
    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="full name")
    tax_domicile = models.CharField(max_length=50, choices=TAX_DOMICILE_CHOICES, blank=True, null=True, verbose_name="tax domicile")
    technical_account = models.CharField(max_length=255, blank=True, null=True, verbose_name="technical account")
    type_of_relationship = models.CharField(max_length=100, choices=RELATIONSHIP_CHOICES, blank=True, null=True, verbose_name="relationship")
    relationship_with_owner = models.CharField(max_length=255, blank=True, null=True, verbose_name="relationship with owner")
    role = models.CharField(max_length=255, blank=True, null=True, verbose_name="role")
    lr_executor = models.CharField(max_length=255, blank=True, null=True, verbose_name="executor")
    lr_beneficial_owner = models.CharField(max_length=255, blank=True, null=True, verbose_name="beneficial owner")
    lr_bo_role = models.CharField(max_length=255, blank=True, null=True, verbose_name="beneficial owner role")
    

    def __str__(self):
        return f"Relation: {self.client_uuid} -> {self.child_unique_id}"

    @property
    def full_name(self):
        """Get the full name of the related client from PersonalInformation."""
        # Try LE first
        try:
            from .models import LE_BankingRelationship
            personal = LE_BankingRelationship.objects.get(client_uuid=self.child_unique_id)
            return personal.name_of_banking_relationship or "N/A"
        except (LE_BankingRelationship.DoesNotExist, ImportError, ValueError):
            
            # Try NP
            try:
                from apps.clients.models import BankingRelationship
                personal = BankingRelationship.objects.get(client_uuid=self.child_unique_id)
                return personal.name_of_banking_relationship or "N/A"
            except (BankingRelationship.DoesNotExist, ValueError):
                return "N/A"

    @property
    def related_banking_relationship(self):
        """Get the banking relationship number of the related client."""
        # Try LE first
        try:
            from .models import LE_BankingRelationship
            related = LE_BankingRelationship.objects.get(client_uuid=self.child_unique_id)
            return related.banking_relationship
        except (LE_BankingRelationship.DoesNotExist, ImportError, ValueError):    
            
            # Try NP
            try:
                from apps.clients.models import BankingRelationship
                related = BankingRelationship.objects.get(client_uuid=self.child_unique_id)
                return related.banking_relationship
            except (BankingRelationship.DoesNotExist, ValueError):
                return "N/A"

    '''@property
    def related_name_of_banking_relationship(self):
        """Get the name of banking relationship of the related client."""
        try:
            related = LE_BankingRelationship.objects.get(client_uuid=self.child_unique_id)
            return related.name_of_banking_relationship
        except LE_BankingRelationship.DoesNotExist:
            return "N/A"

    @property
    def related_first_name(self):
        """Get the first name of the related client from LE_PersonalInformation."""
        try:
            personal = LE_PersonalInformation.objects.get(client_uuid=self.child_unique_id)
            return personal.first_name or "N/A"
        except LE_PersonalInformation.DoesNotExist:
            return "N/A"

    @property
    def related_last_name(self):
        """Get the last name of the related client from LE_PersonalInformation."""
        try:
            personal = LE_PersonalInformation.objects.get(client_uuid=self.child_unique_id)
            return personal.last_name or "N/A"
        except LE_PersonalInformation.DoesNotExist:
            return "N/A"'''

    @property
    def related_client_link(self):
        """Return a clickable link to the related client detail page."""
        from django.utils.safestring import mark_safe
        # Check if it's NP or LE
        from .models import LE_BankingRelationship
        is_le = LE_BankingRelationship.objects.filter(client_uuid=self.child_unique_id).exists()
        
        if is_le:
            url = f"/le/{self.child_unique_id}/"
        else:
            url = f"/clients/{self.child_unique_id}/"
            
        return mark_safe(f'<a href="{url}" class="btn btn-sm btn-outline-primary">click here</a>')

    class Meta:
        verbose_name = "Relationship"
        verbose_name_plural = "Relationships"

class LE_Product(ClientRelatedModel):
    # Choices
    NTAC_CHOICES = [
        ('Excluded', 'Excluded'),
        ('Permitted', 'Permitted'),
    ]
    REPORTING_LOSS_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
    ]
    TYPE_OF_BUSINESS_SETTLEMENT_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Individual', 'Individual'),
    ]
    YES_NO_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Portfolio ID")
    portfolio_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Portfolio Name")
    email_waiver = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Email waiver")
    reference_currency = models.CharField(max_length=10, blank=True, null=True, verbose_name="Currency")
    investment_strategy = models.CharField(max_length=255, blank=True, null=True, verbose_name="Strategy")
    ip_risk_tolerance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Risk tolerance")
    investment_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Investment Service")
    investment_amount = models.CharField(max_length=30, blank=True, null=True,  verbose_name="Investment Amount")
    selected_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Selected Service")
    all_in = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="All In")
    sustainable_investing = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Sustainable Investing")
    sustainability_preference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sustainability preference")
    focus_equity = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Focus")
    alternative_investment = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="alternative investment")
    direct_instrument = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="direct instrument")
    initial_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="initial amount")
    currency_hedging = models.CharField(max_length=100, blank=True, null=True, verbose_name="hedging")
    transaction_confirmation = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="transaction confirmation")
    white_KYC_provided = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="white KYC provided")
    fiduciary_mandate_provided = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="fiduciary mandate provided")
    fiscal_regime = models.CharField(max_length=255, blank=True, null=True, verbose_name="fiscal regime")
    ntac = models.CharField(max_length=50, choices=NTAC_CHOICES, blank=True, null=True, verbose_name="ntac")
    reporting_loss = models.CharField(max_length=50, choices=REPORTING_LOSS_CHOICES, blank=True, null=True, verbose_name="reporting")
    share_focus = models.CharField(max_length=255, blank=True, null=True, verbose_name="share focus")
    hedging_foreign_currency = models.CharField(max_length=255, blank=True, null=True, verbose_name="hedging foreign currency")
    date_of_alignment = models.CharField(max_length=255, blank=True, null=True, verbose_name="align date")
    end_date_alignment = models.DateField(null=True, blank=True, verbose_name="end date")
    type_of_business_settlement = models.CharField(max_length=50, choices=TYPE_OF_BUSINESS_SETTLEMENT_CHOICES, blank=True, null=True, verbose_name="settlement")
    special_conditions = models.TextField(blank=True, null=True, verbose_name="conditions")
    discount_applied = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="discount")
    discount_amount_percent = models.CharField(max_length=255, null=True, blank=True, verbose_name="discount percent")
    flat_fee_applied = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="flat fee")
    flat_fee_percent = models.CharField(max_length=255, null=True, blank=True, verbose_name="flat percent")
    invested_assets = models.CharField(max_length=255, null=True, blank=True, verbose_name="invested")
    income_pa = models.CharField(max_length=255, null=True, blank=True, verbose_name="income")
    current_return_on_assets = models.CharField(max_length=255, null=True, blank=True, verbose_name="return")
    target_roa = models.CharField(max_length=255, null=True, blank=True, verbose_name="target roa")
    net_new_money_potential = models.CharField(max_length=255, null=True, blank=True, verbose_name="net new")
    business_case_communication = models.TextField(blank=True, null=True, verbose_name="business")
    fee_model = models.CharField(max_length=255, blank=True, null=True, verbose_name="fee model")
    mandate_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="mandate")
    service_and_execution = models.CharField(max_length=255, blank=True, null=True, verbose_name="execution")
    no_discount = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="no discount")
    no_discount_amount_percent = models.CharField(max_length=255, null=True, blank=True, verbose_name="no discount percent")
    no_flat_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="no flat")
    no_flat_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="no flat amount")
    transaction_fee = models.CharField(max_length=255, null=True, blank=True, verbose_name="transaction fee")
    standard_fee_discount = models.CharField(max_length=255, null=True, blank=True, verbose_name="standard discount")
    shares_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="shares fee")
    shares_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares fee amount")
    shares_discount = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="shares discount")
    shares_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares discount amount")
    investment_funds_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="funds fee")
    investment_fund_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="funds fee amount")
    investment_fund_discount = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="funds discount")
    investment_fund_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="funds discount amount")
    fixed_income_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="fixed fee")
    fixed_income_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed fee amount")
    fixed_income_discount = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="fixed discount")
    fixed_income_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed discount amount")
    fixed_income_investment_funds_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="fixed funds fee")
    fixed_income_investment_funds_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed funds fee amount")
    fixed_income_investment_funds_discount = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="fixed funds discount")
    fixed_income_investment_funds_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed funds discount amount")
    shares_investment_funds_fee = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="shares funds fee")
    shares_investment_funds_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares funds fee amount")
    shares_investment_funds_discount = models.CharField(max_length=255, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="shares funds discount")
    shares_investment_funds_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares funds discount amount")
    status = models.CharField(max_length=100, blank=True, null=True, verbose_name="status")

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


class LE_Company(ClientRelatedModel):
    """Company information for Legal Entity Clients."""
    type_of_company = models.CharField(max_length=255, null=True, blank=True, verbose_name="type of legal entity")
    name_of_company = models.CharField(max_length=255, null=True, blank=True, verbose_name="name of legal entity")
    ivacf = models.CharField(max_length=255, null=True, blank=True, verbose_name="cf IVA")
    iva = models.CharField(max_length=255, null=True, blank=True, verbose_name="IVA")
    lei_code = models.CharField(max_length=255, null=True, blank=True, verbose_name="LEI Code")
    date_of_constitution = models.DateField(null=True, blank=True, verbose_name="date of constitution")
    place_of_constitution = models.CharField(max_length=255, null=True, blank=True, verbose_name="place of constitution")
    country_of_constitution = models.CharField(max_length=255, null=True, blank=True, verbose_name="country of constitution")
    fiscal_residence = models.CharField(max_length=255, null=True, blank=True, verbose_name="fiscal residence")
    cciaa_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="CCIAA Type")
    cciaa_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="CCIAA Number")
    released_by = models.CharField(max_length=255, null=True, blank=True, verbose_name="Released by")
    date_of_issue = models.DateField(null=True, blank=True, verbose_name="Date of issue")
    form_of_legal_entity = models.CharField(max_length=255, null=True, blank=True, verbose_name="form of legal entity")
    level_of_professionalism = models.CharField(max_length=255, null=True, blank=True, verbose_name="is professional client")
    ateco = models.CharField(max_length=255, null=True, blank=True, verbose_name="ATECO")
    sae = models.CharField(max_length=255, null=True, blank=True, verbose_name="SAE")
    id_third_account_owner = models.CharField(max_length=255, null=True, blank=True, verbose_name="account owner")
    last_name_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="last name")
    first_name_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="first name")
    street_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")
    no_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="number")
    postal_code_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="postal code")
    city_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")
    country_tao = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"



class LE_AdditionalFormDE(ClientRelatedModel):
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
    VALIDITY_CHOICES = [
        ('valid until', 'valid until'),
        ('until canceled', 'until canceled'),
    ]
    YES_NO_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    forward_trading_transactions = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="forward trade")
    exemption_order = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="exemption")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="last name")
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="first name")
    name_at_birth = models.CharField(max_length=255, blank=True, null=True, verbose_name="birth name")
    street = models.CharField(max_length=255, blank=True, null=True, verbose_name="street")
    no = models.CharField(max_length=50, blank=True, null=True, verbose_name="number")
    postal_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="postal code")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="city")
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name="country")
    identification_number = models.BigIntegerField(blank=True, null=True, verbose_name="id number")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="birth date")
    amount = models.CharField(max_length=100, choices=AMOUNT_CHOICES, blank=True, null=True, verbose_name="amount")
    timeline = models.CharField(max_length=100, choices=TIMELINE_CHOICES, blank=True, null=True, verbose_name="timeline")
    date_until = models.DateField(null=True, blank=True, verbose_name="date until")
    valid_as_of = models.DateField(null=True, blank=True, verbose_name="valid from")
    standing_order_form = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="standing order")
    execution = models.CharField(max_length=100, choices=EXECUTION_CHOICES, blank=True, null=True, verbose_name="execution")
    day_of_execution = models.CharField(max_length=50, blank=True, null=True, verbose_name="day")
    first_time_execution = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="first time")
    month = models.IntegerField(blank=True, null=True, verbose_name="month")
    year = models.IntegerField(blank=True, null=True, verbose_name="year")
    validity = models.CharField(max_length=50, choices=VALIDITY_CHOICES, blank=True, null=True, verbose_name="validity")
    valid_until_date = models.DateField(null=True, blank=True, verbose_name="until date")
    tax_at_source_canada = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="tax canada")
    transfer_another_bank = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="transfer bank")