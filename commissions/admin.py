from django.contrib import admin
from .models import Commission, Job, JobApplication

class CommissionAdmin(admin.ModelAdmin):
    model = Commission

class JobAdmin(admin.ModelAdmin):
    model = Job

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
# Register your models here.
