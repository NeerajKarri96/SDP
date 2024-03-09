from django.urls import path, include
from . import views
#test northing is real
#accoding to yt
urlpatterns = [
    path('',views.companyhomepage,name='companyhomepage'),
    path('jobpost',views.Postjob,name='jobpost'),
    path('jobpostdb',views.Postjobdb,name='post_job'),
    path('view',views.view_job_details,name='view_job_details'),
]