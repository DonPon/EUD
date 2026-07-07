"""
This file contains utility functions for exporting and importing repapering settings in JSON format.
The `export_repapering_to_json` function retrieves all scenarios and their associated document requirements,
serializing them into a JSON string. The `import_repapering_from_json` function takes a JSON string, 
deserializes it, and updates or creates scenarios and their document requirements in the database, 
ensuring that existing requirements are replaced with the new ones from the JSON data.
"""
import json
import csv
import io
from django.db import transaction
from .models import Scenario, DocumentRequirement

def export_repapering_to_json():
    data = []
    for scenario in Scenario.objects.all():
        scenario_data = {
            'name': scenario.name,
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
        # Update or create scenarios based on name
        for s_data in data:
            scenario, _ = Scenario.objects.update_or_create(
                name=s_data['name']
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
