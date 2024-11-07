from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .forms import JobFormSet, CommissionForm, JobForm, JobApplicationForm
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
        application_form = JobApplicationForm
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
        context["application_form"] = application_form
        
        return context
    
    def post(self, request, *args, **kwargs):
        job_pk = int(request.POST.get("job_pk"))
        job_application_instance = JobApplication()
        job_application_instance.job = Job.objects.get(pk=job_pk)
        job_application_instance.applicant = self.request.user.profile
        job_application_instance.status = "Pending"
        job_application_instance.save()

        return self.get(request, *args, **kwargs)
    

class CommissionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'commissions/commission_form.html'
    form_class = CommissionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['job_formset'] = JobFormSet(self.request.POST)
        else:
            context['job_formset'] = JobFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.author = self.request.user.profile
        job_formset = context['job_formset']
        if job_formset.is_valid():
            self.object = form.save()
            job_formset.instance = self.object
            job_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ['title','description','status']
    template_name = "commissions/commission_updateform.html"
    
# Create your views here.
