from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    display_name = models.CharField(max_length=63)
    email_add = models.EmailField("Email address")

    def __str__(self):
        return self.display_name
