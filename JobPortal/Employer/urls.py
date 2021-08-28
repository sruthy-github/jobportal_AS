from django.urls import path
from  django.shortcuts import render
from Employer import views



urlpatterns=[
    
    path("login",views.signin,name="signin"),
    path("empadd",views.Emp_Registration.as_view(),name="addemp"),
    path("addjob",views.add_jobs,name="jobadd"),
    path("listjobs",views.job_list,name="listjobs"),
    path("empjobs",views.emp_job,name="emp_jobs"),
    path("remove/<int:id>/",views.DeleteJobs.as_view(),name="delete"),
    path("change/<int:id>/",views.edit_job,name="editjob")
]
