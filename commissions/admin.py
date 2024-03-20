from django.contrib import admin

from .models import Comment, Commission


class CommissionAdmin(admin.ModelAdmin):
    model = Commission


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
