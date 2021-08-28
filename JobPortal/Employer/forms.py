from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Job,Employer
from datetime import datetime


class EmployerRegisterForm(forms.ModelForm):
    class Meta:
        model =Employer
        fields="__all__"
        widgets={
            "f_name":forms.TextInput(attrs={'class':"form-control"}),
            "l_name":forms.TextInput(attrs={'class':"form-control"}),
            "company_name":forms.TextInput(attrs={'class':"form-control"}),
            "company_id":forms.TextInput(attrs={'class':"form-control"}),
            "experience":forms.TextInput(attrs={'class':"form-control"}),
            "contact":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.TextInput(attrs={'class':"form-control"}),
            "gender":forms.Select(attrs={'class':"form-control"}),
            "password":forms.TextInput(attrs={'class':"form-control"})
        }

class JobCreationForm(forms.ModelForm):
    class Meta:
        model=Job
        fields="__all__"
        widgets={
            "company_name":forms.TextInput(attrs={'class':"form-control"}),
            "job_title":forms.TextInput(attrs={'class':"form-control"}),
            "start_date":forms.TextInput(attrs={'class':"form-control"}),
            "end_date":forms.TextInput(attrs={'class':"form-control"}),
            "salary":forms.TextInput(attrs={'class':"form-control"}),
            "comapny_logo":forms.FileInput(attrs={'class':"form-control"}),
            "experience":forms.TextInput(attrs={'class':"form-control"}),
            "location":forms.TextInput(attrs={'class':"form-control"}),
            "skills":forms.TextInput(attrs={'class':"form-control"}),
            "description":forms.Textarea(attrs={'class':"form-control"})
        }
        labels={
            "company_name":"Company Name","job_title":"Job Title","start_date":"Start Date","end_date":"End Date","salary":"Salary","company_logo":"Company Logo","experience":"Experience","location":"Location","skills":"Skills","description":"Description"
        }

class SignInForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(widget=forms.PasswordInput())


