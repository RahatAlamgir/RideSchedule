from django.db import models
from django.contrib.auth.models import User

class user(models.Model ):
    id = models.CharField(max_length=10, primary_key=True,blank=False,null=False)
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 10)
    postal_Code = models.CharField(max_length = 10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    def __str__(self):
        return self.name

class Rider(models.Model):
    rider_id = models.CharField(max_length = 10,primary_key=True,blank=False,null=False)
    id = models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.rider_id
class Driver(models.Model):
    driver_id = models.CharField(max_length=10,primary_key=True,blank=False,null=False)
    id = models.ForeignKey(user, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.driver_id
class Schedule(models.Model):
    schedule_id = models.CharField(max_length=10)
    rider_id1 = models.ForeignKey(Rider,on_delete=models.CASCADE,blank=True,null=True)
    driver_id1 = models.ForeignKey(Driver,on_delete=models.CASCADE,blank=True,null=True)
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




