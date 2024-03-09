from django.shortcuts import render

# Create your views here.
def studenthomepage(request):
    return render(request,'studenthomepage.html')

def applyForJob(request):
    return render(request,'Applyforjob.html')