from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class CreateRiderForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = '__all__'

