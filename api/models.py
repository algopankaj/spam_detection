from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)
    # password = models.CharField(max_length=128)  # modified

class PhoneNumberSpam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    spam_likelihood = models.PositiveIntegerField(default=0)

