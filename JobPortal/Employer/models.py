from django.db import models

# Create your models here.
class Job(models.Model):
    company_name=models.CharField(max_length=100,unique=True)
    job_title=models.CharField(max_length=120)
    start_date=models.DateField()
    end_end=models.DateField()
    salary=models.IntegerField(blank=True)
    company_logo=models.ImageField(upload_to="images")
    experience=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    skills=models.TextField(max_length=120)
    desc=models.TextField(max_length=100)

    def __str__(self):
        return self.company_name
