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
        # Fetch all registered tables metadata for dynamic rendering
        registry = CrudRegistry.get_registered_models()
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
