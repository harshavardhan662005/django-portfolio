from django.shortcuts import render
from .models import Project

def homepage(request):
    # Fetch all project rows out of your MySQL database
    all_projects = Project.objects.all()
    
    # Send those projects over to an HTML file named 'index.html'
    return render(request, 'core/index.html', {'projects': all_projects})