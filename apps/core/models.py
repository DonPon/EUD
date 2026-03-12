from django.db import models
from simple_history.models import HistoricalRecords
import uuid

class BaseUUIDModel(models.Model):
    """Abstract base model with UUID primary key and timestamps."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ClientRelatedModel(BaseUUIDModel):
    """Abstract base model for models related to a client via client_uuid."""
    client_uuid = models.UUIDField(db_index=True)
    
    # Audit logging for all inherited models
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
