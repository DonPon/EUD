from rest_framework import viewsets, permissions, response, filters
from rest_framework.decorators import action
from .registry import CrudRegistry
from .serializers import DynamicSerializerFactory
import django_filters.rest_framework

from .permissions import RoleBasedPermission

class DynamicViewSetFactory:
    @staticmethod
    def _get_default_ordering(model_class):
        field_names = [f.name for f in model_class._meta.fields]
        if 'created_at' in field_names:
            return '-created_at'
        if 'date_joined' in field_names:
            return '-date_joined'
        return 'id'

    @staticmethod
    def create_viewset(model_class, config=None):
        """Create a ModelViewSet for a given model on the fly."""
        config = config or {}
        dynamic_serializer = DynamicSerializerFactory.create_serializer(model_class, config)
        ordering = DynamicViewSetFactory._get_default_ordering(model_class)
        
        class DynamicViewSet(viewsets.ModelViewSet):
            queryset = model_class.objects.all().order_by(ordering)
            serializer_class = dynamic_serializer
            permission_classes = config.get('permission_classes', [RoleBasedPermission])
            filter_backends = [
                django_filters.rest_framework.DjangoFilterBackend,
                filters.OrderingFilter,
                filters.SearchFilter,
            ]
            filterset_fields = config.get('filter_fields', ['client_uuid'])
            search_fields = config.get('search_fields', ['id'])
            ordering_fields = '__all__'

            def get_queryset(self):
                client_uuid = self.request.query_params.get('client_uuid')
                qs = model_class.objects.all().order_by(ordering)
                
                if client_uuid and client_uuid != 'undefined':
                    # Support linking via alternate fields (e.g., bank_rel)
                    filter_field = config.get('client_filter_field', 'client_uuid')
                    
                    if filter_field == 'bank_rel':
                        # Special case: resolving bank_rel from client_uuid
                        from apps.clients.models import BankingRelationship
                        try:
                            client = BankingRelationship.objects.get(client_uuid=client_uuid)
                            qs = qs.filter(bank_rel=client.banking_relationship)
                        except BankingRelationship.DoesNotExist:
                            qs = qs.none()
                    else:
                        filter_kwarg = {filter_field: client_uuid}
                        qs = qs.filter(**filter_kwarg)
                        
                return qs

            def perform_create(self, serializer):
                client_uuid = self.request.data.get('client_uuid') or self.request.query_params.get('client_uuid')
                if client_uuid:
                    serializer.save(client_uuid=client_uuid)
                else:
                    serializer.save()

        viewset_name = f"{model_class.__name__}ViewSet"
        return type(viewset_name, (DynamicViewSet,), {})

from django.views.generic import TemplateView
from django.forms import modelform_factory, DateInput, Select, ChoiceField
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class GenericFormView(LoginRequiredMixin, TemplateView):
    template_name = 'generic_crud/form.html'

    def _get_exclude_fields(self, model, table_name):
        """Standardized list of fields to exclude from forms."""
        exclude = ['id', 'created_at', 'updated_at', 'history', 'last_login', 'date_joined']
        # For User model, exclude fields that shouldn't be edited via generic form
        if table_name == 'user':
            exclude += ['password', 'groups', 'user_permissions', 'is_superuser', 'email']
        # Never show client_uuid in any form; we handle it automatically
        if 'client_uuid' in [f.name for f in model._meta.fields]:
            exclude.append('client_uuid')
        return exclude

    def _apply_dynamic_choices(self, form, model, client_uuid):
        """Inject dynamic choices for fields like product_uuid and child_unique_id."""
        if 'product_uuid' in form.fields and client_uuid:
            try:
                from apps.clients.models import Product
                products = Product.objects.filter(client_uuid=client_uuid)
                choices = [('', '--- Select Product ---')] + [
                    (str(p.id), f"{p.product_name} ({p.product_id})") for p in products
                ]
                # Replace the field with a choice field
                form.fields['product_uuid'] = ChoiceField(
                    choices=choices,
                    label="Product",
                    required=True
                )
                # Apply Bootstrap class to the new field
                form.fields['product_uuid'].widget.attrs.update({'class': 'form-select'})
            except Exception as e:
                print(f"DEBUG: Failed to load product choices: {e}")

        # Handle child_unique_id field for Relationship models
        if 'child_unique_id' in form.fields:
            try:
                # Determine if this is an LE relationship
                is_le = model.__name__ == 'LE_Relationship'
                
                if is_le:
                    from apps.clients_le.models import LE_BankingRelationship, LE_PersonalInformation
                    # Get all LE clients for the dropdown
                    all_clients = LE_BankingRelationship.objects.all().order_by('legal_name')
                else:
                    from apps.clients.models import BankingRelationship, PersonalInformation
                    # Get all NP clients for the dropdown
                    all_clients = BankingRelationship.objects.all().order_by('name_of_banking_relationship')
                
                choices = [('', '--- Select Client ---')]
                for client in all_clients:
                    if is_le:
                        # For LE clients
                        personal = LE_PersonalInformation.objects.filter(client_uuid=client.client_uuid).first()
                        first_name = personal.first_name if personal else ''
                        last_name = personal.last_name if personal else ''
                        display_name = f"{client.banking_relationship} | {client.legal_name or client.name_of_banking_relationship} | {first_name} {last_name}".strip()
                    else:
                        # For NP clients
                        personal = PersonalInformation.objects.filter(client_uuid=client.client_uuid).first()
                        first_name = personal.first_name if personal else ''
                        last_name = personal.last_name if personal else ''
                        display_name = f"{client.banking_relationship} | {client.name_of_banking_relationship} | {first_name} {last_name}".strip()
                    
                    choices.append((str(client.client_uuid), display_name))
                
                # Replace the field with a choice field
                form.fields['child_unique_id'] = ChoiceField(
                    choices=choices,
                    label="Related Client (Banking Relationship | Name | First Last)",
                    required=True
                )
                # Apply Bootstrap class and Select2-friendly attributes
                form.fields['child_unique_id'].widget.attrs.update({
                    'class': 'form-select select2-dropdown',
                    'data-placeholder': 'Search and select a client...'
                })
            except Exception as e:
                print(f"DEBUG: Failed to load client choices for child_unique_id: {e}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_name = self.kwargs.get('table_name', '').lower()
        record_id = self.kwargs.get('pk')
        config = CrudRegistry.get_config(table_name)

        # Always set section, default to 'np' if config not found
        section = config['config'].get('section', 'np') if config else 'np'
        context['section'] = section

        if not config:
            return context

        model = config['model']
        exclude = self._get_exclude_fields(model, table_name)
        
        instance = model.objects.get(id=record_id) if record_id else None
        initial = {}
        client_uuid = self.request.GET.get('client_uuid')
        if client_uuid:
            initial['client_uuid'] = client_uuid

        # Custom widgets for UX and robustness
        widgets = {}
        for field in model._meta.fields:
            internal_type = field.get_internal_type()
            if internal_type == 'DateField':
                widgets[field.name] = DateInput(attrs={'type': 'date'})
            elif internal_type == 'BooleanField':
                widgets[field.name] = Select(choices=[(True, 'Yes'), (False, 'No')])

        form_class = modelform_factory(model, exclude=exclude, widgets=widgets)
        form = kwargs.get('form') or form_class(instance=instance, initial=initial)
        
        # Handle JSONFields that should be Multi-Select
        for field_name in form.fields:
            try:
                model_field = model._meta.get_field(field_name)
                if model_field.get_internal_type() == 'JSONField':
                    # Check if the model has a matching _CHOICES constant
                    choices_attr = f"{field_name.upper()}_CHOICES"
                    if hasattr(model, choices_attr):
                        from django.forms import MultipleChoiceField, SelectMultiple
                        choices = getattr(model, choices_attr)
                        form.fields[field_name] = MultipleChoiceField(
                            choices=choices,
                            widget=SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
                            required=False,
                            initial=getattr(instance, field_name) if instance else []
                        )
            except:
                pass

        # Apply dynamic choices (e.g. Portfolio dropdown)
        self._apply_dynamic_choices(form, model, client_uuid or (instance.client_uuid if instance and hasattr(instance, 'client_uuid') else None))
        
        context.update({
            'form': form,
            'table_name': table_name,
            'verbose_name': model._meta.verbose_name.title(),
            'is_edit': bool(record_id),
            'client_uuid': client_uuid or (instance.client_uuid if instance and hasattr(instance, 'client_uuid') else None),
            'user_role': self.request.user.role,
            'section': section
        })
        return context

    def post(self, request, *args, **kwargs):
        if request.user.role == 'VIEWER':
            return redirect(reverse('clients:list'))

        table_name = self.kwargs.get('table_name', '').lower()
        record_id = self.kwargs.get('pk')
        config = CrudRegistry.get_config(table_name)
        model = config['model']
        section = config['config'].get('section', 'np')

        exclude = self._get_exclude_fields(model, table_name)
        instance = model.objects.get(id=record_id) if record_id else None
        
        widgets = {}
        for field in model._meta.fields:
            internal_type = field.get_internal_type()
            if internal_type == 'DateField':
                widgets[field.name] = DateInput(attrs={'type': 'date'})
            elif internal_type == 'BooleanField':
                widgets[field.name] = Select(choices=[(True, 'Yes'), (False, 'No')])

        form_class = modelform_factory(model, exclude=exclude, widgets=widgets)
        form = form_class(request.POST, instance=instance)
        
        # Re-apply MultipleChoiceField for JSONFields so validation passes
        for field_name in form.fields:
            try:
                model_field = model._meta.get_field(field_name)
                if model_field.get_internal_type() == 'JSONField':
                    choices_attr = f"{field_name.upper()}_CHOICES"
                    if hasattr(model, choices_attr):
                        from django.forms import MultipleChoiceField
                        form.fields[field_name] = MultipleChoiceField(
                            choices=getattr(model, choices_attr),
                            required=False
                        )
            except:
                pass

        # Apply choices for validation
        client_uuid = request.GET.get('client_uuid') or (instance.client_uuid if instance and hasattr(instance, 'client_uuid') else None)
        self._apply_dynamic_choices(form, model, client_uuid)
        
        if form.is_valid():
            obj = form.save(commit=False)
            
            # 1. Handle Client Model (Sync ID and client_uuid)
            if table_name in ['bankingrelationship', 'le_bankingrelationship']:
                if not obj.client_uuid:
                    obj.client_uuid = obj.id
            
            # 2. Handle Related Models (Inject client_uuid from GET param)
            else:
                if client_uuid and hasattr(obj, 'client_uuid'):
                    obj.client_uuid = client_uuid
            
            obj.save()
            print(f"DEBUG: Successfully saved {table_name}: {obj.id}")
            
            # Dynamic redirection based on section
            if hasattr(obj, 'client_uuid') and obj.client_uuid:
                if section == 'le':
                    return redirect(reverse('clients_le:detail', kwargs={'client_uuid': obj.client_uuid}))
                return redirect(reverse('clients:detail', kwargs={'client_uuid': obj.client_uuid}))
            
            if table_name == 'user':
                return redirect(reverse('users:management'))
            
            if section == 'le':
                return redirect(reverse('clients_le:list'))
            return redirect(reverse('clients:list'))
            
        print(f"DEBUG: Form validation failed for {table_name}: {form.errors}")
        return self.render_to_response(self.get_context_data(form=form))

class RegistryMetadataView(viewsets.ViewSet):
    """Provides metadata about registered models for the frontend."""
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def tables(self, request):
        """Returns a list of all registered tables and their config."""
        registered = CrudRegistry.get_registered_models()
        data = {}
        for name, details in registered.items():
            model = details['model']
            config = details['config']
            data[name] = {
                'verbose_name': model._meta.verbose_name.title(),
                'verbose_name_plural': model._meta.verbose_name_plural.title(),
                'columns': self._get_columns(model, config),
                'endpoint': f"/api/table/{name}/"
            }
        return response.Response(data)

    def _get_columns(self, model, config):
        """Helper to extract column configuration for DataTables."""
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
                    'title': field.verbose_name.title(),
                    'type': field.get_internal_type()
                })
            except:
                columns.append({'data': field_name, 'title': field_name.replace('_', ' ').title()})
        return columns
