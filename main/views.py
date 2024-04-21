from django.shortcuts import render ,redirect
from .models import Profile, Schedule
from .scheduleForm import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login as userLogin


def createRider(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        cpassword = request.POST['cpassword']

        address = request.POST['raddress']
        country= request.POST['rcountry']
        phone = request.POST['rphone']
        rate = request.POST['rrate']

        if password==cpassword:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user.profile.isRider = True
            user.profile.address = address
            user.profile.phone = phone
            user.profile.country = country
            user.profile.rate = rate
            user.profile.save()
            user.save()
            return render(request ,'pages/home.html', { 'username': username } )
        
    return render(request , template_name='pages/home.html')
        
# Create your views here.
def home(request):
    return render(request , template_name='pages/home.html')

def profile(request):
    return render(request, template_name='pages/profile.html')

# def schedule(request):
#     form = ScheduleForm()
#     if request.method == 'POST':
#         form = ScheduleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('schedule')

#     context = {
#         'form': form,
#     }
#     return render(request, 'pages/Schedule.html', context=context)

def schedule(request):
    return render(request, template_name='pages/Schedule.html')

def makeSchdedule(request):
    return render(request, template_name='pages/makeSchedule.html')

def help(request):
    return render(request, template_name='pages/help.html')

def contact(request):
    return render(request, template_name='pages/contact.html')

def timeTable(request):
    return render(request, template_name='pages/timeTable.html')

# def schedulePost(request):
#     schedulePost = Schedule.objects.all().order_by("-pickUp_time")

#     posts = {
#         'schedulePost': schedulePost,
#     }
#     return render(request, template_name='pages/SchedulePost.html', context=posts)

def schedulePost(request):
    return render(request, template_name='pages/SchedulePost.html')







