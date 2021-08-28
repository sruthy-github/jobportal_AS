from django.db import models

# Create your models here.

class Employer(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=100)
    company_id=models.CharField(max_length=100)
    experience=models.IntegerField(max_length=15)
    contact=models.TextField(max_length=100)
    email=models.EmailField(max_length=100)
    options=(
        ("male","male"),
        ("female","female"),
        ("TG","TG")
    )
    gender=models.CharField(max_length=100,choices=options,default="male")
    password=models.CharField(max_length=100)



class Job(models.Model):
    company_name=models.CharField(max_length=100,unique=True)
    job_title=models.CharField(max_length=120)
    start_date=models.CharField(max_length=15)
    end_date=models.CharField(max_length=15)
    salary=models.CharField(max_length=120,blank=True)
    company_logo=models.ImageField(upload_to="images")
    experience=models.CharField(max_length=15)
    location=models.CharField(max_length=120)
    skills=models.TextField(max_length=120)
    desc=models.TextField(max_length=100)

    def __str__(self):
        return self.company_name

