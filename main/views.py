from django.shortcuts import render ,redirect
from .models import Profile, Schedule
from .scheduleForm import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='login')
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

@login_required(login_url='login')
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


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context = { 'm1': 'wrong password or username does not exists'}
                return render(request , 'notification/createFail.html' , context)

        
        return redirect('/')
    


def logOutUser(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def profileUpdate(request):
    formU = UserForm()
    formP = ProfileForm()
    user = User.objects.get(username = request.user.username)
    print(user)

    pro = Profile.objects.get( user = user)
    print(pro)
    formU = UserForm(instance = user)
    formP = ProfileForm(instance = pro)
    if request.method == 'POST':
        formU = UserForm(request.POST, request.FILES, instance=user)
        formP = ProfileForm(request.POST, request.FILES, instance=pro)
        if formP.is_valid():
            formP.save()
        if formU.is_valid():
            formU.save()
        return redirect('profile')

    context = {
        'formP':formP,
        'formU':formU
    }

    return render(request, 'update/profileUpdate.html',context)

def changePassword(request):
    form = ChangePassword()
    user = User.objects.get(username = request.user.username)

    form = ChangePassword(instance = user)

    if request.method == 'POST':
        form = ChangePassword(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'update/changePassword.html',{'form': form})

