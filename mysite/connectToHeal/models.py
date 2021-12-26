from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 150)
    date_published = models.DateField('date published');
    blog = models.TextField(default = "")
    cover = models.ImageField(default = 'default.jpg', upload_to = 'blogCovers')
    link = models.URLField(default = "", max_length = 200)
    
    def __str__(self):
        return self.title

class Therapist(models.Model):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    aboutMe = models.CharField(max_length = 1024)
    workExperience = models.CharField(max_length = 1024)
    pricePerSession = models.IntegerField()
    cover = models.ImageField(default = 'default.jpg', upload_to = 'profilephotos')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'aboutMe', 'workExperience','pricePerSession']
    
    def __str__(self):
       return self.username

class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='testinfos', on_delete=models.CASCADE, null=True)
    therapistname = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    date = models.DateField()
    fromtime = models.TimeField()
    totime = models.TimeField()
    paymentstatus = models.CharField(max_length = 100, default = "no")
    sessionstatus = models.CharField(max_length = 100, default = "no")
    notes = models.CharField(max_length = 1024, default = " ")
    
    def __str__(self):
           return self.username + " - " + self.therapistname

class DiscussionModel(models.Model):
    info = models.TextField(max_length = 255)
    def _str_(self):
        return DiscussionModel.objects.count() + 1
