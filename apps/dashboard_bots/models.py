from django.db import models

class Bot(models.Model):
    """Configuration for bots."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BotStatus(models.Model):
    """Current status of each bot."""
    bot = models.CharField(max_length=255, unique=True)
    bot_status = models.CharField(max_length=100)

    class Meta:
        db_table = 'crud_gui_dashboard_bots'
        verbose_name_plural = "Bot Statuses"

    def __str__(self):
        return f"{self.bot}: {self.bot_status}"

class BotRecord(models.Model):
    """Execution records for bots."""
    bot_name = models.CharField(max_length=255)
    bank_rel = models.CharField(max_length=255) # Client BR Number
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    client_type = models.CharField(max_length=100, blank=True, null=True)
    t_number = models.CharField(max_length=100, blank=True, null=True)
    run_identifier = models.CharField(max_length=255, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'crud_gui_dashboard_records_2'

    def __str__(self):
        return f"{self.bot_name} - {self.bank_rel} - {self.status}"
    
    """def save(self, *args, **kwargs):
        if not self.client_uuid:
            # Try to find client by bank_rel (BR Number) if possible
            from apps.clients.models import Client
            try:
                client = Client.objects.get(br_number=self.bank_rel)
                self.client_uuid = client.client_uuid
            except Client.DoesNotExist:
                self.client_uuid = uuid.UUID('00000000-0000-0000-0000-000000000000')
        super().save(*args, **kwargs)"""
