from django.shortcuts import render
from .models import Team

def home(request):
    team_detail= Team.objects.all()

    context= {
        'team_detail' : team_detail,
    }

    return render(request, 'pages/home.html', context)

def about(request):
    team_detail= Team.objects.all()

    context= {
        'team_detail' : team_detail,
    }
    return render(request, 'pages/about.html', context)

def service(request):
    return render(request, 'pages/service.html')

def contact(request):
    return render(request, 'pages/contact.html')
