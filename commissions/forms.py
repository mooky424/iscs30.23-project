from django import forms
from django.forms import formset_factory
from django.forms import ModelForm, TextInput
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    model = Commission
    fields = '__all__'

class JobForm(forms.ModelForm):
    model = Job
    fields = '__all__'