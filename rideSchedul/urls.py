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
    path('schedule/', a_view.schedule , name = 'schedule'),
    path('makeSchedule/', a_view.makeSchdedule , name= 'makeSchedule'),
    path('help/', a_view.help , name = 'help'),
    path('contact/', a_view.contact , name = 'contact'),
    path('schedulePost/', a_view.schedulePost , name = 'schedulePost'),
    path('timeTable/', a_view.timeTable , name = 'timeTable'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
