from django.urls import path, include
from . import views
#test northing is real
#accoding to yt
urlpatterns = [
path('',views.studenthomepage,name='studenthomepage'),
path('apply',views.view_job_details,name='apply'),
path('myProfile',views.myProfile,name='myProfile'),
]