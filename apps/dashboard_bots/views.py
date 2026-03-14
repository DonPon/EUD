from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class DashboardView(LoginRequiredMixin, BotListMixin, TemplateView):
    template_name = 'dashboard_bots/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bots'] = self.get_bot_list()
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
