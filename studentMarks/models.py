from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # set username/identifier to email and not username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]
    currentClass = models.CharField(max_length=2)
    dateOfBirth = models.CharField(max_length=200)
    currentStream = models.CharField(max_length=1)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=250, null=True)
