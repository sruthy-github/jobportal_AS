from django.urls import path
from JobSeeker import views
from django.shortcuts import render



urlpatterns=[
    path("jobseeker/registeruser",views.UserCreationView.as_view(),name="signin"),
    path("jobseeker/login",views.SigninView.as_view(),name="login"),
    path("jobseeker/home",lambda request:render(request,"jshome.html"),name="jshome"),
    path("jobseeker/application",views.ApplicationView.as_view(),name="application"),
    path("jobseeker/joblists",views.JobListView.as_view(),name="joblist")

]