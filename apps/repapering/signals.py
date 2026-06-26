from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import DocumentRequirement

@receiver(post_delete, sender=DocumentRequirement)
def delete_pdf_file(sender, instance, **kwargs):
    if instance.pdf_template:
        instance.pdf_template.delete(save=False)
