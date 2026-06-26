from apps.generic_crud.registry import CrudRegistry
from .models import Scenario, DocumentRequirement

def register_repapering_models():
    CrudRegistry.register(Scenario, {
        'section': 'repapering',
        'fields': ['id', 'name'],
        'list_display': ['name'],
        'search_fields': ['name'],
        'cancel_url_name': 'repapering:scenario_list',
    })

    CrudRegistry.register(DocumentRequirement, {
        'section': 'repapering',
        'fields': [
            'id', 'scenario', 'cdok', 'duplicate', 'granularity', 
            'output_folder_structure', 'pdf_template'
        ],
        'list_display': ['scenario', 'cdok', 'duplicate', 'granularity', 'pdf_template'],
        'search_fields': ['cdok', 'scenario__name'],
        'filter_fields': ['scenario', 'duplicate', 'granularity'],
        'cancel_url_name': 'repapering:scenario_detail', # Needs argument
    })
