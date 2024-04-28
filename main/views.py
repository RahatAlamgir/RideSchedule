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
        
        if password==cpassword and uniqueUserName(username):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user.profile.isRider = True
            user.profile.save()
            user.save()
            context = { 
                    'title':'Welcome',
                    'm1': username,
                    'm2':'your Rider account created successfully',
                    'm3':'Make sure to remember your username or password to Login',
                    'url':'home',
                }
            return render(request , 'notification/message.html' , context)
        else:
            
            context = { 
                    'title':'Fail!',
                    'm1' : 'Account already exists with this Username! or Confirm Password is wrong',
                    'm2': 'Try again',
                    'url':'home',
                }
            return render(request , 'notification/message.html' , context)
        
    return render(request , template_name='pages/home.html')
        
def createDriver(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')


        if password==cpassword and uniqueUserName(username):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            context = { 
                    'title':'Welcome',
                    'm1': username,
                    'm2':'your Driver account created successfully',
                    'm3':'Make sure to remember your username or password to Login',
                    'url':'home',
                }
            return render(request , 'notification/message.html' , context)
        else:
            
            context = { 
                    'title':'Fail!',
                    'm1' : 'Account already exists with this Username! or Confirm Password is wrong',
                    'm2': 'Try again',
                    'url':'home',
                }
            return render(request , 'notification/message.html' , context)
        
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


def makeSchdedule(request):
    return render(request, template_name='pages/makeSchedule.html')

def help(request):
    return render(request, template_name='pages/help.html')


def contact(request):
    return render(request, template_name='pages/contact.html')

@login_required(login_url='login')
def timeTable(request):
    return render(request, template_name='pages/timeTable.html')

@login_required(login_url='login')
def schedulePost(request):
    schedulePost = Schedule.objects.all().order_by("pickUp_time")

    posts = {
        'schedulePost': schedulePost,
    }
    return render(request, template_name='pages/SchedulePost.html', context=posts)




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
                context = { 
                    'title':'Fail!',
                    'm1': 'wrong password or username does not exists',
                    'url':'home',
                }
                return render(request , 'notification/message.html' , context)

        
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
        context = { 
            'title':'Successfull',
            'm1': request.user.username,
            'm2':'your profile Update Successfull',
            'url':'profile',
            }
        return render(request , 'notification/message.html' , context)

    context = {
        'formP':formP,
        'formU':formU
    }

    return render(request, 'update/profileUpdate.html',context)

@login_required(login_url='login')
def changePassword(request):
    form = ChangePassword()
    user = User.objects.get(username = request.user.username)

    form = ChangePassword(instance = user)

    if request.method == 'POST':
        form = ChangePassword(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            context = { 
            'title':'SuccessFull',
            'm1': 'Password change successfull',
            'url':'home',
            }
            return render(request , 'notification/message.html' , context)
        return redirect('/')
    return render(request, 'update/changePassword.html',{'form': form})

@login_required(login_url='login')
def dailySchedule(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='daily',price=price,startDate=startDate,endDate=endDate)
        schedule.save()
        context = { 
            'title':'SuccessFull',
            'm1': 'schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'schedule/dailySchedule.html')

@login_required(login_url='login')
def weeklySchedule(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        week=''
        if(request.POST.get('SUN')): week = week+request.POST.get('SUN')
        if(request.POST.get('MON')): week = week+' '+request.POST.get('MON')
        if(request.POST.get('TUE')): week = week+' '+request.POST.get('TUE')
        if(request.POST.get('WED')): week = week+' '+request.POST.get('WED')
        if(request.POST.get('THE')): week = week+' '+request.POST.get('THE')
        if(request.POST.get('FRI')): week = week+' '+request.POST.get('FRI')
        if(request.POST.get('SAT')): week = week+' '+request.POST.get('SAT')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='weekly',price=price,startDate=startDate,endDate=endDate,weeks=week)
        schedule.save()
        context = { 
            'title':'SuccessFull',
            'm1': 'schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'schedule/weeklySchedule.html')

@login_required(login_url='login')
def allPostSchedule(request):
    schedulePost = Schedule.objects.all().order_by("pickUp_time")

    posts = {
        'schedulePost': schedulePost,
    }
    return render(request,'schedule/allPostSchedule.html',posts)

@login_required(login_url='login')
def deleteSchedule(request , id):
    schedule = Schedule.objects.get(pk = id)
    context={
        'title':'Delete Schedule',
        'm1':'are your sure?',
        'url':'allPostSchedule',
    }
    if request.method == 'POST':
        schedule.delete()
        return redirect('allPostSchedule')
    return render(request, 'notification/confirm.html',context)

@login_required(login_url='login')
def takeSchedule(request , id):
    schedule= Schedule.objects.get(pk = id)
    context={
        'title':'Take Schedule',
        'm2':'Do you want to take this schedule?',
        'text1': 'From: '+schedule.pickup_from +'\n To: '+schedule.drop_to,
        'text2': 'Price: '+str(schedule.price)+'TK',
        'url':'schedulePost',
    }
    if request.method == 'POST':
        schedule.pending = False
        schedule.driver_id = request.user.username
        schedule.save()
        return redirect('schedulePost')
    return render(request, 'notification/confirm.html',context)