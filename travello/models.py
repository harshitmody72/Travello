from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)