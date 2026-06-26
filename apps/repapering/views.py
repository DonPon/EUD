from django.views.generic import ListView, DetailView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Scenario, DocumentRequirement
from apps.generic_crud.registry import CrudRegistry
from .utils import export_repapering_to_json, import_repapering_from_json


class EditorOrAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role in ['ADMIN', 'EDITOR']


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'ADMIN'


class ScenarioListView(LoginRequiredMixin, ListView):
    model = Scenario
    template_name = 'repapering/scenario_list.html'
    context_object_name = 'scenarios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registry_config'] = CrudRegistry.get_config('scenario')
        return context

class ScenarioDetailView(LoginRequiredMixin, DetailView):
    model = Scenario
    template_name = 'repapering/scenario_detail.html'
    context_object_name = 'scenario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        requirements = DocumentRequirement.objects.filter(scenario=self.object)
        context['requirements'] = requirements
        return context

class DocumentRequirementDeleteView(LoginRequiredMixin, EditorOrAdminRequiredMixin, DeleteView):
    model = DocumentRequirement
    
    def get_success_url(self):
        return reverse('repapering:scenario_detail', kwargs={'pk': self.object.scenario.id})

class ExportRepaperingView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        json_data = export_repapering_to_json()
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="repapering_settings.json"'
        return response

class ImportRepaperingView(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            messages.error(request, "No file uploaded.")
            return redirect('repapering:scenario_list')
        
        file = request.FILES['file']
        try:
            json_data = file.read().decode('utf-8')
            import_repapering_from_json(json_data)
            messages.success(request, "Settings imported successfully.")
        except Exception as e:
            messages.error(request, f"Error importing settings: {e}")
        
        return redirect('repapering:scenario_list')

