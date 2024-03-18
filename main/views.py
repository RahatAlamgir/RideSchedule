from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , template_name='pages/home.html')

def profile(request):
    return render(request , template_name='pages/profile.html')

def schedule(request):
    return render(request , template_name='pages/Schedule.html')

def makeSchdedule(request):
    return render(request , template_name='pages/makeSchedule.html')