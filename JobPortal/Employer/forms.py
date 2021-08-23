
from django import forms
from .models import Job
from datetime import datetime

class JobCreationForm(forms.ModelForm):
    class Meta:
        model=Job
        fields="__all__"

        widgets={
            "company_name":forms.TextInput(attrs={'class':"form-control"}),
            "job_title":forms.TextInput(attrs={'class':"form-control"}),
            "start_date":forms.DateInput(attrs={'class':"form-control"}),
            "end_date":forms.DateInput(attrs={'class':"form-control"}),
            "salary":forms.NumberInput(attrs={'class':"form-control"}),
            "comapny_logo":forms.FileInput(attrs={'class':"form-control"}),
            "experience":forms.TextInput(attrs={'class':"form-control"}),
            "location":forms.TextInput(attrs={'class':"form-control"}),
            "skills":forms.TextInput(attrs={'class':"form-control"}),
            "description":forms.Textarea(attrs={'class':"form-control"})
        }
        labels={
            "company_name":"Company Name"
        }
