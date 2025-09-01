from django.shortcuts import render
from .models import Project, Experience

def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    return render(request, "portfolio/home.html", {
        "projects": projects,
        "experiences": experiences
    })
