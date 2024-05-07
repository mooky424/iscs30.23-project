from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Commission


class CommissionListView(LoginRequiredMixin, ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"


# Create your views here.
