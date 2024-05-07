from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from .models import Commission, Job, JobApplication


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission_instance = self.get_object()
        manpower_required = 0
        accepted = 0

        jobs_list = Job.objects.filter(commission=commission_instance)
        for job_instance in jobs_list:
            manpower_required += job_instance.manpower_required
            accepted += JobApplication.objects.filter(status='Accepted',job=job_instance).count()
   
        manpower_available = manpower_required - accepted
        context["total_manpower_required"] = manpower_required
        context["manpower_available"] = manpower_available
        context["accepted"] = accepted
        
        return context

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    fields = '__all__'
    template_name = "commissions/commission_form.html"

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = '__all__'
    template_name = "commissions/commission_form.html"

# Create your views here.
