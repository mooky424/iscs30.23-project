from django.db import models
from django.urls import reverse
from user_management.models import Profile

Status_Choices_Commission = (
    ('Open','Open'), ('Full','Full'), ('Completed','Completed'), ('Discontinued','Discounted')
)

class Commission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'author')
    description = models.TextField()
    people_required = models.IntegerField()
    status = models.CharField(max_length = 12, choices=Status_Choices_Commission, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse("commissions:comItem", args=[str(self.pk)])


Status_Choices_Job = (
    ('Open','Open'), ('Full','Full')
)

class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='job')
    role = models.TextField(max_length = 255)
    manpower_required = models.IntegerField()
    status = models.CharField(max_length = 4, choices=Status_Choices_Job, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['manpower_required']

    def __str__(self):
        return'{}'.format(self.role)

Status_Choices_JobApplicant = (
    ('Pending','Pending'), ('Accepted','Accepted'), ('Rejected','Rejected')
)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='jobapplication')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='jobapplicant')
    status = models.CharField(max_length = 8, choices=Status_Choices_JobApplicant, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return'{}'.format(self.applicant)
# Create your models here.
