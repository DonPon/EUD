from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q
from .models import Bot, BotStatus, BotRecord

class BotListMixin:
    def get_bot_list(self):
        bots = Bot.objects.all()
        bot_list = []
        for bot in bots:
            status_obj = BotStatus.objects.filter(bot=bot.name).first()
            raw_status = status_obj.bot_status if status_obj else 'Unknown'
            
            # Map statuses to "Running" or "Not running"
            display_status = "Running" if raw_status.lower() == "running" else "Not running"
            
            bot_list.append({
                'name': bot.name,
                'description': bot.description,
                'status': display_status
            })
        return bot_list

class ExecutiveSummaryMixin:
    def get_summary_data(self, days=7):
        since = timezone.now() - timedelta(days=days)
        records = BotRecord.objects.filter(created__gte=since)
        
        total_cases = records.count()
        success_cases = records.filter(status__iexact='Success').count()
        error_cases = records.filter(Q(status__iexact='Error') | Q(status__iexact='Failed')).count()
        other_cases = total_cases - success_cases - error_cases
        
        # Stats per bot
        bot_stats = records.values('bot_name').annotate(
            total=Count('id'),
            success=Count('id', filter=Q(status__iexact='Success')),
            error=Count('id', filter=Q(status__iexact='Error') | Q(status__iexact='Failed'))
        ).order_by('-total')
        
        return {
            'total_cases': total_cases,
            'success_cases': success_cases,
            'error_cases': error_cases,
            'other_cases': other_cases,
            'bot_stats': list(bot_stats),
            'days': days
        }

class DashboardView(LoginRequiredMixin, BotListMixin, ExecutiveSummaryMixin, TemplateView):
    template_name = 'dashboard_bots/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        days = int(self.request.GET.get('days', 7))
        context['bots'] = self.get_bot_list()
        context['summary'] = self.get_summary_data(days=days)
        return context

class DashboardBotsPartialView(LoginRequiredMixin, BotListMixin, TemplateView):
    template_name = 'dashboard_bots/_bot_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bots'] = self.get_bot_list()
        return context

class BotDetailsView(LoginRequiredMixin, ListView):
    model = BotRecord
    template_name = 'dashboard_bots/bot_details.html'
    context_object_name = 'records'

    def get_queryset(self):
        return BotRecord.objects.filter(bot_name=self.kwargs['bot_name']).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bot_name'] = self.kwargs['bot_name']
        return context
