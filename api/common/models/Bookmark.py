
from django.db import models
from .Profile import * 

class Bookmark(models.Model):
    link = models.CharField(max_length=512)
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1048576)
