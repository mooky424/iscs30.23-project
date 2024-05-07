from django import forms
from django.forms import ModelForm, TextInput
from .models import Commission, Job, JobApplication

class CommissionForm(forms.Form):
    class Meta:
        model = Commission
        fields = '__all__'

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'