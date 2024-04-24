from django.shortcuts import render ,redirect
from .models import Profile, Schedule
from .scheduleForm import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login as userLogin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def createRider(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        context = {
                'm1' : 'Account already exists with this Username! or Confirm Password is wrong',
                'm2' : 'username already exists',
                'm3' : 'password does not match',
                'username': username
            }

        if password==cpassword and uniqueUserName(username):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user.profile.isRider = True
            user.profile.save()
            user.save()
            return render(request , 'notification/welcome.html' , context)
        else:
            
            return render(request , 'notification/createFail.html' , context)
        
    return render(request , template_name='pages/home.html')
        
# Create your views here.

def createDriver(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        context = {
                'm1' : 'Account already exists with this Username! or Confirm Password is wrong',
                'm2' : 'username already exists',
                'm3' : 'password does not match',
                'username': username
            }

        if password==cpassword and uniqueUserName(username):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request , 'notification/welcome.html' , context)
        else:
            
            return render(request , 'notification/createFail.html' , context)
        
    return render(request , template_name='pages/home.html')

def uniqueUserName(uname):
    users = User.objects.all()
    usernames = [user.username for user in users]

    if uname in usernames:
        return False
    return True

def home(request):
    return render(request , template_name='pages/home.html')

def profile(request):
    return render(request, template_name='pages/profile.html')

def createFail(request):
    return render(request ,template_name='notification/createFail.html')

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







