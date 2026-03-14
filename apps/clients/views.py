from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client
from apps.generic_crud.registry import CrudRegistry
import json

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/client_list.html'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
    slug_field = 'client_uuid'
    slug_url_kwarg = 'client_uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        
        # Fetch all registered tables metadata for dynamic rendering
        registry = CrudRegistry.get_registered_models()
        
        # 1. Prepare Client Information (Top Table)
        client_config = registry.get('client', {}).get('config', {})
        exclude_from_info = client_config.get('exclude_from_info', ['id', 'client_uuid', 'created_at', 'updated_at'])
        
        client_info = []
        for field in client._meta.fields:
            if field.name in exclude_from_info:
                continue
            
            value = getattr(client, field.name)
            # Format choices if applicable
            if field.choices:
                value = dict(field.choices).get(value, value)
            
            client_info.append({
                'label': field.verbose_name.title(),
                'value': value,
                'name': field.name
            })
        
        context['client_info'] = client_info

        # 2. Prepare Metadata for Related Tables
        tables_meta = {}
        for name, details in registry.items():
            if name == 'client': continue # Skip main client
            
            model = details['model']
            config = details['config']
            
            if config.get('is_client_related', True) == False:
                continue
            
            # Use list_display if provided, otherwise exclude internal fields
            fields = config.get('list_display')
            if not fields:
                exclude = ['id', 'client_uuid', 'portfolio_uuid', 'created_at', 'updated_at']
                fields = [f.name for f in model._meta.fields if f.name not in exclude]
                
            columns = []
            for field_name in fields:
                try:
                    field = model._meta.get_field(field_name)
                    columns.append({
                        'data': field_name,
                        'title': field.verbose_name.title()
                    })
                except:
                    columns.append({'data': field_name, 'title': field_name.replace('_', ' ').title()})
            
            tables_meta[name] = {
                'verbose_name': model._meta.verbose_name_plural.title(),
                'columns': columns,
                'endpoint': f"/api/table/{name}/",
                'read_only': config.get('read_only', False)
            }
        
        context['tables_meta_json'] = json.dumps(tables_meta)
        return context
