from django.contrib import admin
from .models import user , Rider,Driver,Schedule
# Register your models here.
admin.site.register([user,Rider,Driver,Schedule])