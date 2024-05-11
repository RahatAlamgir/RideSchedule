from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    rate = models.FloatField(null=True,blank=True)

    isRider = models.BooleanField(default=False)

    image = models.ImageField(upload_to='upload', null=True, blank=True)

    def __str__(self):
        return self.user.username
  

class Schedule(models.Model):
    rider_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    driver_id = models.CharField(blank=True,null=True,max_length=20)
    
    pickUp_time = models.CharField(max_length=10)
    pickup_from = models.CharField(max_length=50)
    drop_to = models.CharField(max_length=50)
    pending = models.BooleanField(default=True)
    schedule_type = (
        ('daily','daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
        ('custom', 'custom'))
    type_of_schedule = models.CharField(max_length=10,choices=schedule_type,blank=True,null=True)
    price = models.IntegerField(blank=True, null=True)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    weeks = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.pickUp_time


class Notification(models.Model):
    user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(blank=True,null=True,max_length=20)
    message = models.CharField(blank=True,null=True,max_length=50)
    
