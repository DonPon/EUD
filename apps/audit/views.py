from rest_framework import viewsets, response, permissions
from rest_framework.decorators import action
from django.views.generic import TemplateView
from apps.generic_crud.registry import CrudRegistry
from django.shortcuts import get_object_or_404
import uuid

class HistoryView(viewsets.ViewSet):
    """View to fetch history for registered tables."""
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='(?P<table_name>[^/.]+)')
    def get_table_history(self, request, table_name):
        """Returns history for all records of a table, optionally filtered by client_uuid."""
        config = CrudRegistry.get_config(table_name)
        if not config:
            return response.Response({"error": "Table not found in registry"}, status=404)
        
        model = config['model']
        client_uuid = request.query_params.get('client_uuid')
        record_id = request.query_params.get('record_id')

        history_qs = model.history.all().order_by('-history_date')
        
        if client_uuid and client_uuid != 'undefined' and client_uuid != 'None':
            history_qs = history_qs.filter(client_uuid=client_uuid)
        if record_id and record_id != 'undefined' and record_id != 'None' and record_id != '{{ record_id }}':
            history_qs = history_qs.filter(id=record_id)

        # Pagination for large history datasets
        page = self.paginate_queryset(history_qs)
        if page is not None:
            # We need to manually construct history data for the page
            data = self._serialize_history(page)
            return self.get_paginated_response(data)

        data = self._serialize_history(history_qs)
        return response.Response(data)

    def _serialize_history(self, history_qs):
        data = []
        # Group by record ID to compute deltas more accurately across versions
        # But for simplicity and server-side processing, we compare version N with version N-1 in the list
        # Simple history's diff_against is useful here.
        
        for i, entry in enumerate(history_qs):
            history_item = {
                'id': entry.history_id,
                'record_id': entry.id if hasattr(entry, 'id') else "N/A",
                'user': str(entry.history_user) if entry.history_user else "System",
                'timestamp': entry.history_date,
                'type': entry.history_type, # + (create), ~ (update), - (delete)
                'changes': []
            }
            
            # To get changes, we need the PREVIOUS historical entry for THIS specific record
            # Not just the previous one in the list.
            prev_entry = entry.prev_record
            if prev_entry:
                delta = entry.diff_against(prev_entry)
                for change in delta.changes:
                    history_item['changes'].append({
                        'field': change.field,
                        'old': str(change.old),
                        'new': str(change.new)
                    })
            else:
                # First version or no previous record
                # Filter out system fields for the first-time display
                exclude = ['history_id', 'history_date', 'history_user', 'history_type', 'history_change_reason']
                for field in entry.instance._meta.fields:
                    if field.name not in exclude:
                        history_item['changes'].append({
                            'field': field.name,
                            'old': None,
                            'new': str(getattr(entry, field.name))
                        })
            
            data.append(history_item)
        return data

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            from rest_framework.pagination import LimitOffsetPagination
            self._paginator = LimitOffsetPagination()
        return self._paginator

    def paginate_queryset(self, queryset):
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)

class HistoryListView(TemplateView):
    """Template view to render the History DataTables page."""
    template_name = 'audit/history_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_name = self.kwargs.get('table_name')
        client_uuid = self.request.GET.get('client_uuid')
        
        config = CrudRegistry.get_config(table_name)
        if config:
            model = config['model']
            context['verbose_name'] = model._meta.verbose_name.title()
            context['verbose_name_plural'] = model._meta.verbose_name_plural.title()
            context['section'] = config.get('section', 'np')
        
        context['table_name'] = table_name
        context['client_uuid'] = client_uuid
        context['record_id'] = self.request.GET.get('record_id')
        return context
