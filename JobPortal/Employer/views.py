from django.shortcuts import render,redirect
from Employer import forms as employerforms
from django.contrib import messages
from django.views.generic import ListView,DeleteView,CreateView
from django.urls import reverse_lazy
from Employer import forms
from django.contrib.auth import authenticate,login,logout

from .models import Job,Employer

# Create your views here.
class Emp_Registration(CreateView):
    model = Employer
    form_class = forms.EmployerRegisterForm
    template_name = "empregistration.html"
    success_url = reverse_lazy("signin")

def add_jobs(request):
    form=employerforms.JobCreationForm()
    context={}
    context={"form":form}
    if request.POST:
        form=employerforms.JobCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"new job added")
            return redirect("jobadd")

        else:
            messages.error(request, "something went wrong")
            return render(request, "create_job.html", {"form": form})
    return render(request,"create_job.html",context)

def get_objects(id):
    return Job.objects.get(id=id)

def job_list(request):
    jobs=Job.objects.all()
    context={"jobs":jobs}
    return render(request,"jobview.html",context)

def emp_job(requesst):
    jobs=Job.objects.all()
    context={"jobs":jobs}
    return render(requesst,"emp_joblist.html",context)

class DeleteJobs(DeleteView):
    model = Job
    template_name = "delete_job.html"
    context_object_name = "jobs"
    success_url = reverse_lazy("emp_jobs")

def edit_job(request,id):
    job=get_objects(id)
    form=employerforms.JobCreationForm(instance=job)
    context={"form":form}
    if request.method=="POST":
        form=employerforms.JobCreationForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("emp_jobs")
        else:
            context={"form":form}
            messages.error(request,"failed to edit")
            return render(request,"update.html",context)
    return render(request, "update.html", context)



def signin(request):
    form=forms.SignInForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.SignInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_authenticated:
                    return redirect("emphome")
                return redirect("jshome")
            else:
                context["form"]=form
                return render(request,"login.html",context)
    return render(request,"login.html",context)






