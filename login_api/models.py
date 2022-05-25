from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Interesting_Club(models.Model):
    name = models.CharField(max_length=20)

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    major = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    interesting = models.ManyToManyField(Interesting_Club)

    REQUIRED_FIELDS = []