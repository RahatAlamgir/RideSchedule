from django import forms
from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','address','country','image']

class ChangePassword(ModelForm):
    class Meta:
        model = User
        fields = '__all__'