from django.shortcuts import render

# Create your views here.
#projecthomepage
def adminhomepage(request):
    return render(request,'adminhomepage.html')