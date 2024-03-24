from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user(models.Model):
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 10)
    postal_Code = models.CharField(max_length = 10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
