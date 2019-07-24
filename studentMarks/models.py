from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    currentClass = models.CharField(max_length=2)
    emailAddress = models.CharField(max_length=200, unique=True)
    dateOfBirth = models.CharField(max_length=200)
    currentStream = models.CharField(max_length=1)
    password = models.CharField(max_length=200, null=True)
