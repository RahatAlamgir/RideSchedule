"""
URL configuration for rideSchedul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as a_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',a_view.home , name = 'home'),
    path('home/', a_view.home , name = 'home'),
    path('profile/', a_view.profile , name = 'profile'),
    path('makeSchedule/', a_view.makeSchdedule , name= 'makeSchedule'),
    path('help/', a_view.help , name = 'help'),
    path('contact/', a_view.contact , name = 'contact'),
    path('schedulePost', a_view.schedulePost , name = 'schedulePost'),
    path('timeTable/', a_view.timeTable , name = 'timeTable'),
    path('policy', a_view.policy, name = 'policy'),
    path('rateUs', a_view.rateUs, name = 'rateUs'),


    path('createRider', a_view.createRider , name = 'createRider'),
    path('createDriver', a_view.createDriver , name = 'createDriver'),
    path('loginUser',a_view.loginUser,name='loginUser'),
    path('logOutUser', a_view.logOutUser, name='logOutUser'),
    path('profileUpdate', a_view.profileUpdate, name='profileUpdate'),
    path('changePassword',a_view.changePassword, name='changePassword'),
    path('dailySchedule',a_view.dailySchedule, name='dailySchedule'),


    path('weeklySchedule',a_view.weeklySchedule, name='weeklySchedule'),
    path('monthlySchedule',a_view.monthlySchedule, name='monthlySchedule'),
    path('allPostSchedule',a_view.allPostSchedule, name='allPostSchedule'),


    path('deleteSchedule <str:id>', a_view.deleteSchedule, name='deleteSchedule'),
    path('takeSchedule <str:id>',a_view.takeSchedule,name='takeSchedule'),
    path('deleteNotification <str:id>',a_view.deleteNotification,name='deleteNotification'),
    path('updateSchedule <str:id>',a_view.updateSchedule,name='updateSchedule'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
