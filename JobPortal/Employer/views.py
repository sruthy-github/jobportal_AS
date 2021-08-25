from django.shortcuts import render,redirect
from Employer import forms as employerforms
from django.contrib import messages
from django.views.generic import ListView

from .forms import JobCreationForm
from .models import Job

# Create your views here.
def add_jobs(request):
    form=employerforms.JobCreationForm()
    context={"form":form}
    if request.POST:
        form=JobCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "new job added")
            return redirect("jobadd")

        else:
            messages.error(request, "something went wrong")
            return render(request, "create_job.html", {"form": form})
    return render(request,"create_job.html",context)

def job_list(request):
    jobs=Job.objects.all()
    context={"jobs":jobs}
    return render(request,"jobview.html",context)


