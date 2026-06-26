from django.db import models
from simple_history.models import HistoricalRecords
from apps.core.models import BaseUUIDModel

class Scenario(BaseUUIDModel):
    name = models.CharField(max_length=255, help_text='e.g. "A - Natural Person Resident"')
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name}"

class DocumentRequirement(BaseUUIDModel):
    GRANULARITY_CHOICES = [
        ("One for each Co-owner", "One for each Co-owner"),
        ("One for each BO", "One for each BO"),
        ("One for each LR", "One for each LR"),
        ("One for each POA", "One for each POA"),
    ]

    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='requirements')
    cdok = models.CharField(max_length=100, verbose_name="Document Code (CDOK)")
    duplicate = models.BooleanField(default=False)
    granularity = models.CharField(max_length=255, choices=GRANULARITY_CHOICES, null=True, blank=True)
    output_folder_structure = models.CharField(max_length=500, blank=True, null=True)
    pdf_template = models.FileField(upload_to='repapering_templates/', blank=True, null=True, verbose_name="PDF Template")
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.scenario.name} - {self.cdok}"
