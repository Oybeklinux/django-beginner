from django.shortcuts import render
from .models import *
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