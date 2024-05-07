from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Commission, Job, JobApplication


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for job_instance in Job.objects.all():
            manpower_required = job_instance.manpower_required
            accepted = JobApplication.objects.filter(status='Accepted',job=job_instance).count()
            manpower_available = manpower_required - accepted

        context["manpower_available"] = manpower_available
        context["accepted"] = accepted
        
        return context

# Create your views here.
