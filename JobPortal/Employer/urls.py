from django.urls import path
from  django.shortcuts import render,redirect
from Employer import views


urlpatterns=[
    path("addjob",views.add_jobs,name="jobadd")
]
