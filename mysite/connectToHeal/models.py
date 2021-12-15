from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 150)
    date_published = models.DateField('date published');
    blog = models.TextField(default = "")
    cover = models.ImageField(default = 'default.jpg', upload_to = 'blogCovers')
    link = models.URLField(default = "", max_length = 200)
    def __str__(self):
        return self.title