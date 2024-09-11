from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_subscriber = models.BooleanField(default=False)
    is_trial = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    def __str__(self):
        return self.username
