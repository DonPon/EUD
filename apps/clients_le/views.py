from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LE_BankingRelationship, LE_PersonalInformation, LE_Company
from apps.generic_crud.registry import CrudRegistry
import json

class LE_CompleteReviewView(LoginRequiredMixin, View):
    def post(self, request, client_uuid):
        client = get_object_or_404(LE_BankingRelationship, client_uuid=client_uuid)
        status_list = client.status or []
        
        if 'pending_review' in status_list:
            # Remove pending_review
            status_list = [s for s in status_list if s != 'pending_review']
            # Add review_completed if not already there
            if 'review_completed' not in status_list:
                status_list.append('review_completed')
            
            client.status = status_list
            client.save()
            
        return redirect('clients_le:detail', client_uuid=client_uuid)

class BulkStatusUpdateLEView(LoginRequiredMixin, View):
    def post(self, request):
        client_ids = request.POST.getlist('client_ids[]')
        new_statuses = request.POST.getlist('statuses[]')
        
        if client_ids and new_statuses is not None:
            LE_BankingRelationship.objects.filter(id__in=client_ids).update(status=new_statuses)
            
        return redirect('clients_le:list')

class BulkDeleteLEView(LoginRequiredMixin, View):
    def post(self, request):
        if request.user.role != 'ADMIN':
            return redirect('clients_le:list')
            
        client_ids = request.POST.getlist('client_ids[]')
        if client_ids:
            LE_BankingRelationship.objects.filter(id__in=client_ids).delete()
            
        return redirect('clients_le:list')

class LE_ClientListView(LoginRequiredMixin, ListView):
    model = LE_BankingRelationship
    template_name = 'clients_le/client_list.html'
    context_object_name = 'clients'

class LE_ClientDetailView(LoginRequiredMixin, DetailView):
    model = LE_BankingRelationship
    template_name = 'clients_le/client_detail.html'
    context_object_name = 'client'
    slug_field = 'client_uuid'
    slug_url_kwarg = 'client_uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        
        # Pre-format status badges
        status_badges = []
        choices_dict = dict(LE_BankingRelationship.STATUS_CHOICES)
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

        registry = CrudRegistry.get_registered_models()
        
        # 1. Prepare Hub Info (LE_BankingRelationship)
        client_info = []
        exclude = ['id', 'client_uuid', 'created_at', 'updated_at']
        for field in client._meta.fields:
            if field.name in exclude: continue
            value = getattr(client, field.name)
            if field.choices: value = dict(field.choices).get(value, value)
            elif isinstance(value, list): value = ", ".join(map(str, value))
            
            client_info.append({
                'label': field.verbose_name.title(),
                'value': value,
                'name': field.name
            })
        context['client_info'] = client_info

        # 2. Prepare LE Personal Information (Legal Entity specific details)
        le_info_obj = LE_PersonalInformation.objects.filter(client_uuid=client.client_uuid).first()
        le_info_list = []
        if le_info_obj:
            for field in le_info_obj._meta.fields:
                if field.name in exclude: continue
                value = getattr(le_info_obj, field.name)
                if field.choices: value = dict(field.choices).get(value, value)
                le_info_list.append({
                    'label': field.verbose_name.title(),
                    'value': value,
                    'name': field.name
                })
        context['personal_info'] = le_info_list # Reusing template variable name for consistency
        context['personal_info_obj'] = le_info_obj

        # 3. Prepare Company Information
        company_obj = LE_Company.objects.filter(client_uuid=client.client_uuid).first()
        company_info_list = []
        if company_obj:
            for field in company_obj._meta.fields:
                if field.name in exclude: continue
                value = getattr(company_obj, field.name)
                if field.choices: value = dict(field.choices).get(value, value)
                company_info_list.append({
                    'label': field.verbose_name.title(),
                    'value': value,
                    'name': field.name
                })
        context['company_info'] = company_info_list
        context['company_info_obj'] = company_obj

        # 4. Prepare Related Tables Metadata
        tables_meta = {}
        registry = CrudRegistry.get_registered_models(section='le')
        for name, details in registry.items():
            # Only include LE related tables that are not the main ones
            if name not in ['le_bankingrelationship', 'le_personalinformation', 'le_company']:
                model = details['model']
                config = details['config']
                
                fields = config.get('list_display')
                if not fields:
                    fields = [f.name for f in model._meta.fields if f.name not in exclude]
                
                columns = []
                for field_name in fields:
                    try:
                        field = model._meta.get_field(field_name)
                        columns.append({'data': field_name, 'title': field.verbose_name.title()})
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
