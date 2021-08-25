from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from JobSeeker.models import Application
from JobSeeker import forms
# Create your views here.


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






