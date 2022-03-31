from django.shortcuts import redirect, render
from .models import *
from .forms import ProjectForm
# Create your views here.


def projects(request):

    reviews_p = Review.objects.filter(value="+")
    reviews_m = Review.objects.filter(value="-")
    projects = Project.objects.filter(project_review__isnull=True)
    context = {
        "projects": projects,
        "reviews_p": reviews_p,
        "reviews_m": reviews_m
    }
    return render(request, "projects/projects.html", context)


def project(request, id):
    project = Project.objects.get(id=id)
    tags = project.tag.all()
    context = {
        "project": project,
        "tags": tags
    }
    return render(request, "projects/project.html", context)


def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')    
    form = ProjectForm()
    context = {
        "form": form
    }
    return render(request, "projects/project_add.html", context)

def project_edit(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')    
    
    context = {
        "form": form
    }
    return render(request, "projects/project_add.html", context)