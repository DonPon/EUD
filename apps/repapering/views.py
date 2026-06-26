from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import Scenario, DocumentRequirement
from apps.generic_crud.registry import CrudRegistry

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

class DocumentRequirementDeleteView(LoginRequiredMixin, DeleteView):
    model = DocumentRequirement
    
    def get_success_url(self):
        return reverse('repapering:scenario_detail', kwargs={'pk': self.object.scenario.id})

