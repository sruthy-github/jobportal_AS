from django.urls import path
from JobSeeker import views
from django.shortcuts import render



urlpatterns=[
    path("jobseeker/home",lambda request:render(request,"jshome.html"),name="jshome"),
    path("jobseeker/application",views.ApplicationView.as_view(),name="application"),

]