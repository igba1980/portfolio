from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from .models import Job


def joblist(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/detail.html', {'job': job})


def homepage(request):
    return render(request, 'jobs/homepage.html')
