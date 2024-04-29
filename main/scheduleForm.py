from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ScheduleUpdateForm(ModelForm):
    class meta:
        model = Schedule
        # fields = ['pickUp_time','pickup_from','drop_to','type_of_schedule','price','startDate','endDate','weeks']
        fields = '__all__'



