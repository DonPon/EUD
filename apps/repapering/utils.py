import json
import csv
import io
from django.db import transaction
from .models import Scenario, DocumentRequirement

def export_repapering_to_json():
    data = []
    for scenario in Scenario.objects.all():
        scenario_data = {
            'scenario_id': scenario.scenario_id,
            'name': scenario.name,
            'description': scenario.description,
            'requirements': []
        }
        for req in scenario.requirements.all():
            scenario_data['requirements'].append({
                'cdok': req.cdok,
                'duplicate': req.duplicate,
                'granularity': req.granularity,
                'output_folder_structure': req.output_folder_structure,
                'pdf_template': req.pdf_template.name if req.pdf_template else None
            })
        data.append(scenario_data)
    return json.dumps(data, indent=4)

def import_repapering_from_json(json_data):
    data = json.loads(json_data)
    with transaction.atomic():
        # Optional: Decide if we should clear existing scenarios or just update
        # For this implementation, we'll update scenarios and replace requirements
        for s_data in data:
            scenario, _ = Scenario.objects.update_or_create(
                scenario_id=s_data['scenario_id'],
                defaults={
                    'name': s_data['name'],
                    'description': s_data['description']
                }
            )
            # Replace all requirements
            scenario.requirements.all().delete()
            for r_data in s_data['requirements']:
                DocumentRequirement.objects.create(
                    scenario=scenario,
                    cdok=r_data['cdok'],
                    duplicate=r_data['duplicate'],
                    granularity=r_data['granularity'],
                    output_folder_structure=r_data['output_folder_structure'],
                    pdf_template=r_data['pdf_template']
                )
