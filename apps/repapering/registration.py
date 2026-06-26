from apps.generic_crud.registry import CrudRegistry
from .models import Scenario, DocumentRequirement

def register_repapering_models():
    CrudRegistry.register(Scenario, {
        'section': 'repapering',
        'fields': ['id', 'name'],
        'list_display': ['name'],
        'search_fields': ['name'],
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
    })
