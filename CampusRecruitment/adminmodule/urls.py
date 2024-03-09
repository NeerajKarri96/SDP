from django.contrib import admin
from django.urls import path, include
from . import views

#accoding to yt
urlpatterns = [
path('',views.adminhomepage,name='adminhomepage')
]