from django import forms
from django.forms import ModelForm
from .models import Application,MyUser
from .admin import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["email","username"]

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())

class ApplicationForm(ModelForm):
    class Meta:
        model=Application
        fields=['job_title','candidate_name','age','dob','email','phone_number',
                'qualification','college','percent_or_cgpa']
        widgets={
            'job_title':forms.Select(attrs={'class':'form-select'}),
            'candidate_name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'college':forms.TextInput(attrs={'class':'form-control'}),
            'percent_or_cgpa':forms.NumberInput(attrs={'class':'form-control'})
        }
        labels={
            "job_title":"Job Title","candidate_name":"Candidate Name","age":"Age","dob":"Date of Birth",
                  "email":"E-mail","phone_number":"Phone Number","qualification":"Qualification",
            "college":"College","percent_or_cgpa":"Percentage or CGPA"
        }
