from django.contrib import admin
from .models import Profile,Schedule
# Register your models here.
admin.site.register([Profile,Schedule])