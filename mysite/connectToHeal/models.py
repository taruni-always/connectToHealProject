from django.db import models
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
    
class DiscussionModel(models.Model):
    info = models.TextField(max_length = 255)
    def _str_(self):
        return DiscussionModel.objects.count() + 1
'''
class Therapist(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    native_name = models.CharField(max_length = 5)
    aboutMe = models.CharField(max_length = 1024)
    workExperience = models.CharField(max_length = 1024)
    pricePerSession = models.IntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'pricePerSession']
    def __str__(self):
       return "{}".format(self.email)'''