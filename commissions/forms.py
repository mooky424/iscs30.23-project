from django import forms
from django.forms import inlineformset_factory
from django.forms import ModelForm, TextInput
from .models import Commission, Job, JobApplication


Status_Choices_Commission = (
    ('Open','Open'), ('Full','Full'), ('Completed','Completed'), ('Discontinued','Discounted')
)

class CommissionForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices = Status_Choices_Commission)
    class Meta:
        model = Commission
        fields = ['title','description','status']

class JobForm(forms.ModelForm):
    role = forms.CharField(max_length=255)
    manpower_required = forms.IntegerField()
    class Meta:
        model = Job
        fields = ['role','manpower_required']

JobFormSet = inlineformset_factory(Commission, Job, form=JobForm, extra = 3)

Status_Choices_JobApplicant = (
    ('Pending','Pending'), ('Accepted','Accepted'), ('Rejected','Rejected')
)

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
