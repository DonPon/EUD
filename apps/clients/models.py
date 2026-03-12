from django.db import models
from apps.core.models import ClientRelatedModel

class Client(ClientRelatedModel):
    """The central Client model for the Bank."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    br_number = models.CharField(max_length=50, unique=True, verbose_name="Business Relation (BR)")
    date_of_birth = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[('active', 'Active'), ('inactive', 'Inactive'), ('frozen', 'Frozen')],
        default='active'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.br_number})"

    def save(self, *args, **kwargs):
        if not self.client_uuid:
            self.client_uuid = self.id
        super().save(*args, **kwargs)

class Nationality(ClientRelatedModel):
    country = models.CharField(max_length=100)
    is_main = models.BooleanField(default=False, verbose_name="Main Nationality")

    class Meta:
        verbose_name_plural = "Nationalities"

class Address(ClientRelatedModel):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_main = models.BooleanField(default=False, verbose_name="Main Address")
    is_domicile = models.BooleanField(default=False, verbose_name="Domicile Address")
    is_tax_domicile = models.BooleanField(default=False, verbose_name="Tax Domicile")
    tin = models.CharField(max_length=50, blank=True, null=True, verbose_name="TIN Number")

    class Meta:
        verbose_name_plural = "Addresses"

class Communication(ClientRelatedModel):
    class Type(models.TextChoices):
        PHONE = 'PHONE', 'Phone'
        EMAIL = 'EMAIL', 'Email'
    
    comm_type = models.CharField(max_length=10, choices=Type.choices)
    value = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False, verbose_name="Main Contact")

class Portfolio(ClientRelatedModel):
    portfolio_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

class Account(ClientRelatedModel):
    portfolio_uuid = models.UUIDField(db_index=True)
    account_number = models.CharField(max_length=50, unique=True)
    currency = models.CharField(max_length=3, default='USD')
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    @property
    def portfolio_info(self):
        """Virtual field to show portfolio details in tables without a hard FK."""
        try:
            # We import inside to avoid circular dependencies
            from .models import Portfolio
            p = Portfolio.objects.get(id=self.portfolio_uuid)
            return f"{p.portfolio_number} ({p.name})"
        except:
            return "N/A"
