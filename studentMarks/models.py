from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    currentClass = models.CharField(max_length=2)
    dateOfBirth = models.CharField(max_length=200)
    currentStream = models.CharField(max_length=1)
    password = models.CharField(max_length=250, null=True)
