from apps.generic_crud.registry import CrudRegistry
from .models import Scenario, DocumentRequirement

def register_repapering_models():
    CrudRegistry.register(Scenario, {
        'section': 'repapering',
        'fields': ['id', 'scenario_id', 'name', 'description'],
        'list_display': ['scenario_id', 'name'],
        'search_fields': ['scenario_id', 'name'],
    })

    CrudRegistry.register(DocumentRequirement, {
        'section': 'repapering',
        'fields': [
            'id', 'scenario', 'cdok', 'duplicate', 'granularity', 
            'output_folder_structure', 'pdf_template', 
            'rules_special_conditions'
        ],
        'list_display': ['scenario', 'cdok', 'duplicate', 'granularity', 'pdf_template'],
        'search_fields': ['cdok', 'scenario__scenario_id', 'scenario__name'],
        'filter_fields': ['scenario', 'duplicate', 'granularity'],
        'read_only_fields': ['rules_special_conditions'],
    })
