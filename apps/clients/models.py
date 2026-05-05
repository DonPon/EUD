import uuid
from django.db import models
from apps.core.models import ClientRelatedModel

class BankingRelationship(ClientRelatedModel):
    """The Hub for the Star Schema architecture."""
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

    # Required Fields from Table
    name_of_banking_relationship = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name Banking Relationship")
    banking_relationship = models.CharField(max_length=255, blank=True, null=True, verbose_name="Banking Relationship")
    additional_br = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional Banking Relationship")
    partner_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Partner ID")
    type_of_account = models.CharField(max_length=50, choices=TYPE_OF_ACCOUNT_CHOICES, blank=True, null=True, verbose_name="Type of Account")
    type_of_signature = models.CharField(max_length=50, choices=SIGNATURE_CHOICES, blank=True, null=True, verbose_name="Type of Signature")
    segment_type = models.CharField(max_length=10, choices=SEGMENT_TYPE_CHOICES, null=True, blank=True)
    client_segment = models.CharField(max_length=50, blank=True, null=True, verbose_name="Client Segment")
    code_ksc = models.CharField(max_length=50, blank=True, null=True, verbose_name="Client Segment Code (CSC)")
    communication_br = models.CharField(max_length=50, choices=COMMUNICATION_BR_CHOICES, blank=True, null=True, verbose_name="Communication mode")
    third_postal_address = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Third Postal Address")
    beneficial_owner = models.CharField(max_length=50, choices=BENEFICIAL_OWNER_CHOICES, blank=True, null=True, verbose_name="Beneficial Owner")
    id_doc_provided = models.CharField(max_length=50, choices=ID_DOC_PROVIDED_CHOICES, blank=True, null=True, verbose_name="ID copy provided")
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, blank=True, null=True, verbose_name="Language")
    opened_in_ubs_premises = models.CharField(max_length=50, choices=OPENED_IN_UBS_PREMISES_CHOICES, blank=True, null=True, verbose_name="Account Opening Location")
    account_and_securities_statements = models.CharField(max_length=100, choices=ACCOUNT_STATEMENTS_CHOICES, blank=True, null=True, verbose_name="transaction statements")
    type_and_purpose = models.CharField(max_length=100, choices=TYPE_AND_PURPOSE_CHOICES, blank=True, null=True, verbose_name="Purpose of Banking Relations")
    type_and_purpose_specify = models.CharField(max_length=255, blank=True, null=True, verbose_name="Details of Purpose")
    reporting_obligation = models.CharField(max_length=50, choices=REPORTING_OBLIGATION_CHOICES, blank=True, null=True, verbose_name="Reporting Accordance")
    br_client_type = models.CharField(max_length=50, choices=BR_CLIENT_TYPE_CHOICES, blank=True, null=True, verbose_name="Client Type")
    earning_statements = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Earnings Statements")
    earning_statements_fees = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Fees")
    fiscal_identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fiscal Identifier")
    agreement_distribution_fees = models.CharField(max_length=100, choices=AGREEMENT_FEES_CHOICES, blank=True, null=True, verbose_name="Distribution Fees Agreement")
    agreement_percentage = models.CharField(max_length=255, blank=True, null=True, verbose_name="Percentage For The Client")
    number_of_portfolios = models.IntegerField(choices=NUMBER_OF_PORTFOLIOS_CHOICES, null=True, blank=True, verbose_name="Number of Portfolios")
    delivery_date = models.DateField(null=True, blank=True, verbose_name="Delivery Date")
    time = models.TimeField(null=True, blank=True, verbose_name="Time")
    document_format = models.CharField(max_length=255, blank=True, null=True, verbose_name="Document Format")
    distance_mode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Distance Mode")
    ateco = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ateco")
    sae = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sae")
    level_of_professionalism = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="Professional Client")
    send_documents = models.CharField(max_length=50, choices=SEND_DOCUMENTS_CHOICES, blank=True, null=True, verbose_name="Sending Documents")
    further_notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    status = models.JSONField(default=list, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.client_uuid:
            self.client_uuid = uuid.uuid4()
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
    postal_code = models.IntegerField(blank=True, null=True, verbose_name="postal code")
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

class PersonalInformation(ClientRelatedModel):
    ROLE_CHOICES = [
        ('Owner', 'Owner'),
        ('Co-owner', 'Co-owner'),
        ('POA (for all accounts)', 'POA (for all accounts)'),
        ('POA (general)', 'POA (general)'),
        ('POA (limited)', 'POA (limited)'),
        ('POA (in case of death)', 'POA (in case of death)'),
        ('Beneficial Owner', 'Beneficial Owner'),
    ]
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    technical_account = models.CharField(max_length=255, blank=True, null=True, verbose_name="type of legal entity")
    type_of_relationship = models.CharField(max_length=100, choices=ROLE_CHOICES, blank=True, null=True, verbose_name="role in Banking Relationship")
    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First and last name")
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="first name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="last name")
    name_at_birth = models.CharField(max_length=255, blank=True, null=True, verbose_name="name at birth")
    type_id_NCI = models.CharField(max_length=255, blank=True, null=True, verbose_name="type of identification (NCI)")
    fiscal_it_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fiscal code IT (number)")
    type_id_document = models.CharField(max_length=255, blank=True, null=True, verbose_name="Type of ID Document")
    release_authority = models.CharField(max_length=255, blank=True, null=True, verbose_name="release authority")
    release_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="release place")
    release_date = models.DateField(null=True, blank=True, verbose_name="release date")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="expiry date")
    copy_id_provided = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="copy of ID provided")
    place_of_birth = models.CharField(max_length=255, blank=True, null=True, verbose_name="Place of birth")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of birth")
    country_of_birth = models.CharField(max_length=255, blank=True, null=True, verbose_name="Country of birth")
    marital_status = models.CharField(max_length=100, blank=True, null=True, verbose_name="marital status")
    occupation_sector = models.CharField(max_length=255, blank=True, null=True, verbose_name="occupation")
    fiscal_identifier = models.CharField(max_length=255, blank=True, null=True, verbose_name="fiscal identifier")
    fiscal_residence = models.CharField(max_length=255, blank=True, null=True, verbose_name="fiscal residence")
    has_ebanking = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="has ebanking")
    sensitive_client = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="sensitive client")

class Address(ClientRelatedModel):
    TYPE_CHOICES = [
        ('Correspondence', 'Correspondence'),
        ('Domicile', 'Domicile'),
    ]
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="full name")
    type_of_address = models.CharField(max_length=100, choices=TYPE_CHOICES, blank=True, null=True, verbose_name="address type")
    c_o = models.CharField(max_length=255, blank=True, null=True, verbose_name="c/o")
    street = models.CharField(max_length=255, blank=True, null=True, verbose_name="street")
    no = models.CharField(max_length=50, blank=True, null=True, verbose_name="number")
    postal_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="postal code")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="city")
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name="province")
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name="country")
    annual_tax_cert = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="tax certificates")
    receive_copies_of_original = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="copy mail")
    third_party_copies = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="third copy")

    class Meta:
        verbose_name_plural = "Addresses"

class Communication(ClientRelatedModel):
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

    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="full name")
    type_of_communication = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True, null=True, verbose_name="type")
    communication_context = models.CharField(max_length=255, choices=CONTEXT_CHOICES, blank=True, null=True, verbose_name="context")
    prefix = models.CharField(max_length=20, blank=True, null=True, verbose_name="prefix")
    number = models.CharField(max_length=255, blank=True, null=True, verbose_name="number")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="address")

class ClientAdvisor(ClientRelatedModel):
    ROLE_CHOICES = [
        ('Requestor', 'Requestor'),
        ('Client Advisor', 'Client Advisor'),
        ('Deputy Client Advisor', 'Deputy Client Advisor'),
    ]
    role_client_advisor = models.CharField(max_length=100, choices=ROLE_CHOICES, blank=True, null=True, verbose_name="role")
    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="full name")
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="first name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="last name")
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="email")
    branch = models.CharField(max_length=255, blank=True, null=True, verbose_name="branch")
    distribution_list = models.CharField(max_length=255, blank=True, null=True, verbose_name="distribution")

class Nationality(ClientRelatedModel):
    is_main_nationality = models.BooleanField(default=False, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    nci = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=255, blank=True, null=True)
    fiscal_code = models.CharField(max_length=255, blank=True, null=True)
    fiscal_code_path = models.CharField(max_length=255, blank=True, null=True)
    release_authority = models.CharField(max_length=255, blank=True, null=True)
    release_location = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    is_id_document_provided = models.BooleanField(default=False, blank=True, null=True)
    id_document_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Nationalities"

class TIN(ClientRelatedModel):
    aei_tin = models.CharField(max_length=255, blank=True, null=True, verbose_name="AEI/TIN")

    class Meta:
        verbose_name = "TIN"
        verbose_name_plural = "TINs"

class EBanking(ClientRelatedModel):
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="first name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="last name")
    access_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="access type")
    contract_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="contract")

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
    YES_NO_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    place = models.CharField(max_length=50, choices=PLACE_CHOICES, blank=True, null=True, verbose_name="place")
    date_of_meeting = models.DateField(null=True, blank=True, verbose_name="meeting date")
    time = models.TimeField(null=True, blank=True, verbose_name="time")
    number_of_participants = models.IntegerField(null=True, blank=True, verbose_name="participants")
    room_booking = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="room booking")
    hospitality = models.CharField(max_length=100, choices=HOSPITALITY_CHOICES, blank=True, null=True, verbose_name="hospitality")
    technical_equipment_needed = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="equipment")
    parking_space_client = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="parking")
    pool_car = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="pool car")
    from_date = models.DateField(null=True, blank=True, verbose_name="from date")
    from_time = models.TimeField(null=True, blank=True, verbose_name="from time")
    to_date = models.DateField(null=True, blank=True, verbose_name="to date")
    to_time = models.TimeField(null=True, blank=True, verbose_name="to time")
    planned_contact = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="planned contact")
    contact_CST = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="cst contact")
    stored_reporting_t2_ptf = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="stored report")
    performance_since_beginning = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="since begin")
    performance_before_tax = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="before tax")
    performance_since_start = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="since start")
    health_check = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="health check")
    remarks_documents = models.CharField(max_length=255, blank=True, null=True, verbose_name="remarks")
    investor_profile_link = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="profile link")
    email_waiver = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True, verbose_name="email waiver")

class Relationship(ClientRelatedModel):
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
    ]

    child_unique_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="child id")
    first_and_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="full name")
    tax_domicile = models.CharField(max_length=50, choices=TAX_DOMICILE_CHOICES, blank=True, null=True, verbose_name="tax domicile")
    technical_account = models.CharField(max_length=255, blank=True, null=True, verbose_name="technical account")
    type_of_relationship = models.CharField(max_length=100, choices=RELATIONSHIP_CHOICES, blank=True, null=True, verbose_name="relationship")
    relationship_with_owner = models.CharField(max_length=255, blank=True, null=True, verbose_name="relationship with owner")

    def __str__(self):
        return f"Relation: {self.client_uuid} -> {self.child_unique_id}"
    @property
    def full_name(self):
        """Get the full name of the related client from PersonalInformation."""
        try:
            from .models import BankingRelationship
            personal = BankingRelationship.objects.get(client_uuid=self.child_unique_id)
            return personal.name_of_banking_relationship or "N/A"
        except (BankingRelationship.DoesNotExist, ValueError):
            return "N/A"
    @property

    def related_banking_relationship(self):
        """Get the banking relationship number of the related client."""
        try:
            related = BankingRelationship.objects.get(client_uuid=self.child_unique_id)
            return related.banking_relationship
        except (BankingRelationship.DoesNotExist, ValueError):
            return "N/A"

    '''@property
    def related_name_of_banking_relationship(self):
        """Get the name of banking relationship of the related client."""
        try:
            related = BankingRelationship.objects.get(client_uuid=self.child_unique_id)
            return related.name_of_banking_relationship
        except (BankingRelationship.DoesNotExist, ValueError):
            return "N/A"

    @property
    def related_first_name(self):
        """Get the first name of the related client from PersonalInformation."""
        try:
            from .models import PersonalInformation
            personal = PersonalInformation.objects.get(client_uuid=self.child_unique_id)
            return personal.first_name or "N/A"
        except (PersonalInformation.DoesNotExist, ValueError):
            return "N/A"

    @property
    def related_last_name(self):
        """Get the last name of the related client from PersonalInformation."""
        try:
            from .models import PersonalInformation
            personal = PersonalInformation.objects.get(client_uuid=self.child_unique_id)
            return personal.last_name or "N/A"
        except (PersonalInformation.DoesNotExist, ValueError):
            return "N/A"'''

    @property
    def related_client_link(self):
        """Return a clickable link to the related client detail page."""
        from django.utils.safestring import mark_safe
        url = f"/clients/{self.child_unique_id}/"
        return mark_safe(f'<a href="{url}" class="btn btn-sm btn-outline-primary">click here</a>')

class Product(ClientRelatedModel):
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
    email_waiver = models.BooleanField(default=False, null=True, blank=True, verbose_name="Email waiver")
    reference_currency = models.CharField(max_length=10, blank=True, null=True, verbose_name="Currency")
    investment_strategy = models.CharField(max_length=255, blank=True, null=True, verbose_name="Strategy")
    ip_risk_tolerance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Risk tolerance")
    investment_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Investment Service")
    investment_amount = models.CharField(max_length=255, blank=True, null=True,  verbose_name="Investment Amount")
    selected_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Selected Service")
    all_in = models.BooleanField(default=False, null=True, blank=True, verbose_name="All In")
    sustainable_investing = models.BooleanField(default=False, null=True, blank=True, verbose_name="Sustainable Investing")
    sustainability_preference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sustainability preference")
    focus_equity = models.BooleanField(default=False, null=True, blank=True, verbose_name="Focus")
    alternative_investment = models.BooleanField(default=False, null=True, blank=True, verbose_name="alternative investment")
    direct_instrument = models.BooleanField(default=False, null=True, blank=True, verbose_name="direct instrument")
    initial_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="initial amount")
    currency_hedging = models.CharField(max_length=100, blank=True, null=True, verbose_name="hedging")
    transaction_confirmation = models.BooleanField(default=False, null=True, blank=True, verbose_name="transaction confirmation")
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
    discount_applied = models.BooleanField(default=False, null=True, blank=True, verbose_name="discount")
    discount_amount_percent = models.CharField(max_length=255, null=True, blank=True, verbose_name="discount percent")
    flat_fee_applied = models.BooleanField(default=False, null=True, blank=True, verbose_name="flat fee")
    flat_fee_percent = models.CharField(max_length=255, null=True, blank=True, verbose_name="flat percent")
    invested_assets = models.CharField(max_length=255, null=True, blank=True, verbose_name="invested")
    income_pa = models.CharField(max_length=255, null=True, blank=True, verbose_name="income")
    current_return_on_assets = models.CharField(max_length=255, null=True, blank=True, verbose_name="return")
    target_roa = models.CharField(max_length=255, null=True, blank=True, verbose_name="target roa")
    net_new_money_potential = models.CharField(max_length=255, null=True, blank=True, verbose_name="net new")
    business_case_communication = models.TextField(blank=True, null=True, verbose_name="business")
    fee_model = models.CharField(max_length=255, blank=True, null=True, verbose_name="fee model")
    mandate_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="mandate")
    service_and_execution = models.CharField(max_length=255, blank=True, null=True, verbose_name="execution")
    no_discount = models.BooleanField(default=False, null=True, blank=True, verbose_name="no discount")
    no_discount_amount_percent = models.CharField(max_length=255, null=True, blank=True, verbose_name="no discount percent")
    no_flat_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="no flat")
    no_flat_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="no flat amount")
    transaction_fee = models.CharField(max_length=255, null=True, blank=True, verbose_name="transaction fee")
    standard_fee_discount = models.CharField(max_length=255, null=True, blank=True, verbose_name="standard discount")
    shares_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="shares fee")
    shares_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares fee amount")
    shares_discount = models.BooleanField(default=False, null=True, blank=True, verbose_name="shares discount")
    shares_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares discount amount")
    investment_funds_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="funds fee")
    investment_fund_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="funds fee amount")
    investment_fund_discount = models.BooleanField(default=False, null=True, blank=True, verbose_name="funds discount")
    investment_fund_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="funds discount amount")
    fixed_income_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="fixed fee")
    fixed_income_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed fee amount")
    fixed_income_discount = models.BooleanField(default=False, null=True, blank=True, verbose_name="fixed discount")
    fixed_income_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed discount amount")
    fixed_income_investment_funds_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="fixed funds fee")
    fixed_income_investment_funds_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed funds fee amount")
    fixed_income_investment_funds_discount = models.BooleanField(default=False, null=True, blank=True, verbose_name="fixed funds discount")
    fixed_income_investment_funds_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="fixed funds discount amount")
    shares_investment_funds_fee = models.BooleanField(default=False, null=True, blank=True, verbose_name="shares funds fee")
    shares_investment_funds_fee_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares funds fee amount")
    shares_investment_funds_discount = models.BooleanField(default=False, null=True, blank=True, verbose_name="shares funds discount")
    shares_investment_funds_discount_amount = models.CharField(max_length=255, null=True, blank=True, verbose_name="shares funds discount amount")
    status = models.CharField(max_length=100, blank=True, null=True, verbose_name="status")

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
