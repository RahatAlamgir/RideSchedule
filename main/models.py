from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    rate = models.FloatField(null=True,blank=True)

    isRider = models.BooleanField(default=False)

    image = models.ImageField(upload_to='upload', null=True, blank=True)

    def __str__(self):
        return self.user.username
  

class Schedule(models.Model):
    rider_id = models.CharField(null=True, blank=True,max_length=20)
    driver_id = models.CharField(blank=True,null=True,max_length=20)
    
    pickUp_time = models.CharField(max_length=10)
    pickup_from = models.CharField(max_length=50)
    drop_to = models.CharField(max_length=50)
    schedule_type = (
        ('daily','daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
        ('custom', 'custom'))
    type_of_schedule = models.CharField(max_length=10,choices=schedule_type,blank=True,null=True)
    price = models.IntegerField(blank=True, null=True)
    startDate = models.CharField(max_length=30,blank=True,null=True)
    endDate = models.CharField(max_length=30,blank=True,null=True)




