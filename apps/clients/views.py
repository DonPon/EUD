from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BankingRelationship
from apps.generic_crud.registry import CrudRegistry
import json

class CompleteReviewView(LoginRequiredMixin, View):
    def post(self, request, client_uuid):
        client = get_object_or_404(BankingRelationship, client_uuid=client_uuid)
        status_list = client.status or []
        
        if 'pending_review' in status_list:
            # Remove pending_review
            status_list = [s for s in status_list if s != 'pending_review']
            # Add review_completed if not already there
            if 'review_completed' not in status_list:
                status_list.append('review_completed')
            
            client.status = status_list
            client.save()
            
        return redirect('clients:detail', client_uuid=client_uuid)

class BulkStatusUpdateView(LoginRequiredMixin, View):
    def post(self, request):
        client_ids = request.POST.getlist('client_ids[]')
        new_statuses = request.POST.getlist('statuses[]')
        
        if client_ids and new_statuses is not None:
            BankingRelationship.objects.filter(id__in=client_ids).update(status=new_statuses)
            
        return redirect('clients:list')

class BulkDeleteView(LoginRequiredMixin, View):
    def post(self, request):
        if request.user.role != 'ADMIN':
            return redirect('clients:list')
            
        client_ids = request.POST.getlist('client_ids[]')
        if client_ids:
            # Force evaluation of the QuerySet by converting to a list.
            # Otherwise, deleting from BankingRelationship first would make the QuerySet empty
            # for subsequent models in the loop.
            client_uuids = list(BankingRelationship.objects.filter(id__in=client_ids).values_list('client_uuid', flat=True))
            
            if client_uuids:
                from django.apps import apps
                client_app = apps.get_app_config('clients')
                for model in client_app.get_models():
                    # Every model in this app inherits from ClientRelatedModel and has client_uuid
                    model.objects.filter(client_uuid__in=client_uuids).delete()
            
        return redirect('clients:list')

class ClientListView(LoginRequiredMixin, ListView):
    model = BankingRelationship
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = BankingRelationship
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'
    slug_field = 'client_uuid'
    slug_url_kwarg = 'client_uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        
        # Pre-format status badges for header
        status_badges = []
        choices_dict = dict(BankingRelationship.STATUS_CHOICES)
        for s in (client.status or []):
            cls = 'bg-secondary'
            if s == 'pending_review': cls = 'bg-warning text-dark'
            elif s == 'review_completed': cls = 'bg-success'
            elif 'ready_for_bot' in s: cls = 'bg-info text-dark'
            elif s == 'completed': cls = 'bg-success'
            elif s == 'pending_docs': cls = 'bg-danger'
            
            status_badges.append({
                'label': choices_dict.get(s, s.replace('_', ' ').upper()),
                'class': cls
            })
        context['status_badges'] = status_badges

        # Fetch all registered tables metadata for dynamic rendering
        registry = CrudRegistry.get_registered_models(section='np')
        
        # 1. Prepare Client Information (Top Table)
        client_config = registry.get('bankingrelationship', {}).get('config', {})
        exclude_from_info = client_config.get('exclude_from_info', ['id', 'client_uuid', 'created_at', 'updated_at'])
        
        client_info = []
        for field in client._meta.fields:
            if field.name in exclude_from_info:
                continue
            
            value = getattr(client, field.name)
            
            # Format JSON list fields (e.g. status)
            if isinstance(value, list):
                choices_attr = f"{field.name.upper()}_CHOICES"
                if hasattr(BankingRelationship, choices_attr):
                    choices_dict = dict(getattr(BankingRelationship, choices_attr))
                    value = ", ".join([choices_dict.get(v, v) for v in value])
                else:
                    value = ", ".join(map(str, value))
            
            # Format single choices if applicable
            elif field.choices:
                value = dict(field.choices).get(value, value)
            
            client_info.append({
                'label': field.verbose_name.title(),
                'value': value,
                'name': field.name
            })
        
        context['client_info'] = client_info

        # 1.1 Prepare Personal Information (Second Top Table)
        from .models import PersonalInformation
        personal_info_obj = PersonalInformation.objects.filter(client_uuid=client.client_uuid).first()
        personal_info_list = []
        
        if personal_info_obj:
            exclude_personal = ['id', 'client_uuid', 'created_at', 'updated_at']
            for field in personal_info_obj._meta.fields:
                if field.name in exclude_personal:
                    continue
                
                value = getattr(personal_info_obj, field.name)
                if field.choices:
                    value = dict(field.choices).get(value, value)
                
                personal_info_list.append({
                    'label': field.verbose_name.title(),
                    'value': value,
                    'name': field.name
                })
        
        context['personal_info'] = personal_info_list
        context['personal_info_obj'] = personal_info_obj

        # 2. Prepare Metadata for Related Tables
        tables_meta = {}
        for name, details in registry.items():
            if name in ['bankingrelationship', 'personalinformation']: continue # Skip main tables
            
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
