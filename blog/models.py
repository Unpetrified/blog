from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from turtle import title
from django.db import models
from datetime import datetime


class Post(models.Model):
    author = models.CharField(default="", max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField(default="", max_length=1000000)
    photo = models.ImageField(upload_to='images/')