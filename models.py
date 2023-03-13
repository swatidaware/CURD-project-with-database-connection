from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)