from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]

    list_display = [
        "username",
        "display_name",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    ]

    def display_name(self, obj):
        return obj.profile.display_name


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
