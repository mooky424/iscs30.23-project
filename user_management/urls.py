from django.urls import path

from .views import ProfileUpdateView

urlpatterns = [
    path("", ProfileUpdateView.as_view(), name="profile_update"),
]

app_name = "profile"
