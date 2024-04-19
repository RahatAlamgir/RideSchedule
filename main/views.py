from django.shortcuts import render ,redirect
from .models import user, Driver, Rider, Schedule
from .scheduleForm import *


# Create your views here.
def home(request):
    return render(request , template_name='pages/home.html')

def profile(request):
    return render(request, template_name='pages/profile.html')

def schedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('schedule')

    context = {
        'form': form,
    }
    return render(request, 'pages/Schedule.html', context=context)

def makeSchdedule(request):
    return render(request, template_name='pages/makeSchedule.html')

def help(request):
    return render(request, template_name='pages/help.html')

def contact(request):
    return render(request, template_name='pages/contact.html')

def timeTable(request):
    return render(request, template_name='pages/timeTable.html')

def schedulePost(request):
    schedulePost = Schedule.objects.all().order_by("-pickUp_time")

    posts = {
        'schedulePost': schedulePost,
    }
    return render(request, template_name='pages/SchedulePost.html', context=posts)







