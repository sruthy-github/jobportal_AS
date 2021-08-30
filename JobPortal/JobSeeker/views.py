from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from JobSeeker.models import Application,MyUser
from JobSeeker import forms
from Employer.models import Job
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class UserCreationView(CreateView):
    template_name = "register.html"
    model=MyUser
    form_class=forms.RegistrationForm
    success_url=reverse_lazy("jshome")

class SigninView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=forms.LoginForm
        return context

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)

            # if user:
            #     login(request,user)
            #     if request.user.role=="faculty":
            #         return redirect("fhome")
            #     else:
            #         return redirect("courseadd")
        else:
            return render(request,self.template_name,{'form':form})

class ApplicationView(TemplateView):
    model=Application
    form_class=forms.ApplicationForm
    template_name = 'application.html'
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            job_title=form.cleaned_data['job_title']
            candidate_name=form.cleaned_data['candidate_name']
            age=form.cleaned_data['age']
            dob=form.cleaned_data['dob']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            qualification=form.cleaned_data['qualification']
            college=form.cleaned_data['college']
            percent_or_cgpa=form.cleaned_data['percent_or_cgpa']
            app=self.model()
            app.job_title=job_title
            app.candidate_name=candidate_name
            app.age=age
            app.dob=dob
            app.email=email
            app.phone_number=phone_number
            app.qualification=qualification
            app.college=college
            app.percent_or_cgpa=percent_or_cgpa
            app.save()
            return redirect("jshome")
        else:
            self.context['form']=form
            return render(request,self.template_name,self.context)

class JobListView(TemplateView):
    model=Job
    template_name = "joblist.html"
    context={}
    def get(self, request, *args, **kwargs):
        jobs=self.model.objects.all()
        self.context["jobs"]=jobs
        return render(request,self.template_name,self.context)






