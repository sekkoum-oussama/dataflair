from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length = 50, default = 'From administration')
    title = models.CharField(max_length = 100)
    content = models.TextField()
    published = models.BooleanField(default = False)