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
        ('Registered Office', 'Registered Office'),
        ('Business Address', 'Business Address'),
        ('Correspondence', 'Correspondence'),
        ('Tax Domicile', 'Tax Domicile'),
    ]
    type_of_address = models.CharField(max_length=100, choices=TYPE_CHOICES, blank=True)
    street = models.CharField(max_length=255, blank=True)
    no = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "LE Address"
        verbose_name_plural = "LE Addresses"

class LE_Communication(ClientRelatedModel):
    department = models.CharField(max_length=255, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    email_address = models.EmailField(blank=True, null=True)
    fax_address = models.CharField(max_length=255, blank=True)
    pec_address = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = "LE Communication"
        verbose_name_plural = "LE Communications"
