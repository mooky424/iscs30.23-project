from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import ProfileForm
from .models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile/profile_update.html"

    def get_object(self):
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def form_valid(self, form):
        form.instance.user = self.object.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("merchstore:product_list")
