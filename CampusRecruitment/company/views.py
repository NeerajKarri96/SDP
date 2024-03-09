from django.shortcuts import render
from .models import Jobdetails
# Create your views here.
def companyhomepage(request):
    return render(request,'companyhomepage.html')

def Postjob(request):
    return render(request,'Postjob.html')

#add jobdetails to db
def Postjobdb(request):
    if request.method == 'POST':
        job_title=request.POST.get('job_title')
        job_des=request.POST.get('job_des')
        job_req = request.POST.get('job_req')
        work_loc = request.POST.get('work_loc')
        app_email = request.POST.get('app_email')

        job_details=Jobdetails(
            job_title=job_title,
            job_des=job_des,
            job_req=job_req,
            work_loc=work_loc,
            app_email=app_email,
        )
        job_details.save()
        return render(request,'Postjob.html')
    return render(request,'Postjob.html')

#to view data from db
def view_job_details(request):
    job_details_list=Jobdetails.objects.all()
    return render(request,'ViewJobdetails.html',{'job_details_list':job_details_list})

