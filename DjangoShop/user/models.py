from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    wallet = models.IntegerField(default=10000)

    def __str__(self):
        return self.username
