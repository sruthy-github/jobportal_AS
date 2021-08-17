from django.shortcuts import render,redirect
from Employer import forms as employerforms
from django.contrib import messages


# Create your views here.
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
            messages.error(request,"something went wrong,unable to add new job")
            return redirect(request,"create_job.html",{"form":form})
    return render(request,"create_job.html",context)




