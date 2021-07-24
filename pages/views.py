from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)
## 'teams' is the name of variable teams, be used in other pages, commented by Tung

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
