from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    currentClass = models.CharField(max_length=2)
    emailAddress = models.CharField(max_length=200, unique=True)
    dateOfBirth = models.CharField(max_length=200)
    currentStream = models.CharField(max_length=1)
