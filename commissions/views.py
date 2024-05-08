from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Comment, Commission


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

class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    template_name = "commissions/commission_form.html"
    form_class = JobApplicationForm

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.job = Job.objects.get(self.job.get_pk)
        form.instance.applicant = self.request.user.profile
        
        return super().form_valid(form)
# Create your views here.
