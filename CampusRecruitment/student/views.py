from django.shortcuts import render

from django.db import models
from .models import *
from django.contrib import *

from company.models import Jobdetails


# Create your views here.
def studenthomepage(request):
    return render(request,'studenthomepage.html')

def applyForJob(request):
    return render(request,'Applyforjob.html')

def myProfile(request):
    return render(request,'myProfile.html')


def view_job_details(request):
    job_details_list = Jobdetails.objects.all()
    return render(request, 'Applyforjob.html', {'job_details_list': job_details_list})