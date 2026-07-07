"""
This file contains signal handlers for the DocumentRequirement model. 
It ensures that when a DocumentRequirement instance is deleted, its associated PDF template file 
is also deleted from the storage. Additionally, it handles the case where a PDF template is updated, 
ensuring that the old file is removed to prevent orphaned files in the storage.
"""

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import DocumentRequirement

@receiver(post_delete, sender=DocumentRequirement)
def delete_pdf_file(sender, instance, **kwargs):
    if instance.pdf_template:
        try:
            instance.pdf_template.delete(save=False)
        except Exception:
            pass

@receiver(pre_save, sender=DocumentRequirement)
def cleanup_old_pdf(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = DocumentRequirement.objects.get(pk=instance.pk)
            if old_instance.pdf_template and old_instance.pdf_template != instance.pdf_template:
                old_instance.pdf_template.delete(save=False)
        except DocumentRequirement.DoesNotExist:
            pass
