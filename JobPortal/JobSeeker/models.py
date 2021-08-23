from django.db import models
from Employer.models import Job
# Create your models here.



class Application(models.Model):
    job_title=models.ForeignKey(Job,on_delete=models.CASCADE)
    candidate_name=models.CharField(max_length=80)
    age=models.IntegerField()
    dob=models.CharField(max_length=80)
    email=models.EmailField(max_length=120)
    phone_number=models.IntegerField()
    qualification=models.CharField(max_length=80)
    college=models.CharField(max_length=120)
    percent_or_cgpa=models.IntegerField()

    def __str__(self):
        return self.candidate_name