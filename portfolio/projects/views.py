from django.shortcuts import redirect, render
from .models import *
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profil
            project.save()
            return redirect('projects')    
    form = ProjectForm()
    context = {
        "form": form
    }
    return render(request, "projects/project_add.html", context)

@login_required(login_url='login')
def project_edit(request, id):
    profile = request.user.profil # o'zgarish
    try:# o'zgarish
        project = profile.project_set.get(id=id)# o'zgarish
    except Project.DoesNotExist:# o'zgarish
        messages.warning(request, "Faqat o'zingizga tegishli loyihanigina o'zgartira olasiz")# o'zgarish
        return redirect('projects')# o'zgarish

    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')    
    
    context = {
        "form": form
    }
    return render(request, "projects/project_add.html", context)

@login_required(login_url='login')
def project_delete(request, id):
    profile = request.user.profil
    try:
        project = profile.project_set.get(id=id)
    except Project.DoesNotExist:
        messages.warning(request, "Faqat o'zingizga tegishli loyihanigina o'chira olasiz")
        return redirect('account')
    
    project.delete()
    return redirect('account')
