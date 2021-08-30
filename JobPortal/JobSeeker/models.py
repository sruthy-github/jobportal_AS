from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager
from Employer.models import Job
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email=models.EmailField(max_length=120,unique=True)
    username=models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

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
    options=(("Applied","Applied"),("Accepted","Accepted"),("Rejected","Rejected"))
    status=models.CharField(max_length=120,choices=options,default="Applied")

    def __str__(self):
        return self.candidate_name

class JsProfile(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    age=models.IntegerField()
    dob=models.CharField(max_length=80)
    email=models.EmailField(max_length=120)
    ten_board=models.CharField(max_length=120)
    ten_school=models.CharField(max_length=120)
    ten_percent=models.IntegerField()
    twelve_board=models.CharField(max_length=80)
    twelve_school=models.CharField(max_length=88)
    twelve_percent=models.IntegerField()
    degree_university=models.CharField(max_length=90)
    degree_college=models.CharField(max_length=90)
    degree_cgpa_or_mark=models.IntegerField()
    skills=models.TextField(max_length=200)
    resume=models.FileField(upload_to="files")