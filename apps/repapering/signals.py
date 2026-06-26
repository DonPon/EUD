import json
import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Scenario, DocumentRequirement

CONFIG_FILE_PATH = os.path.join(settings.BASE_DIR, 'repapering_config.json')

def update_config_file():
    data = {
        'scenarios': [],
        'document_requirements': []
    }
    
    for scenario in Scenario.objects.all():
        data['scenarios'].append({
            'scenario_id': scenario.scenario_id,
            'name': scenario.name,
            'description': scenario.description,
        })
        
    for req in DocumentRequirement.objects.all():
        data['document_requirements'].append({
            'scenario_id': req.scenario.scenario_id,
            'cdok': req.cdok,
            'duplicate': req.duplicate,
            'granularity': req.granularity,
            'output_folder_structure': req.output_folder_structure,
            'input_filename': req.input_filename,
            'pdf_template': req.pdf_template.url if req.pdf_template else None,
            'rules_special_conditions': req.rules_special_conditions,
        })
        
    with open(CONFIG_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

@receiver(post_save, sender=Scenario)
@receiver(post_delete, sender=Scenario)
@receiver(post_save, sender=DocumentRequirement)
@receiver(post_delete, sender=DocumentRequirement)
def sync_to_config_file(sender, **kwargs):
    update_config_file()
