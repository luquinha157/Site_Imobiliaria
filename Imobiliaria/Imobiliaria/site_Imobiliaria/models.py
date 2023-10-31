from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
# class Imoveis(models.Model):
#   addres = models.CharField(max_length= 40)
#   status = models.EmailField(max_length= 40)
#   area = models.CharField(max_length= 11)
#   bedrooms = models.CharField(default='4002-8922', max_length=14)
#   bathrooms = models.CharField(max_length= 40)
#   floor = models.TextField(max_length=255)
#   parking = models.CharField(max_length= 20, default='1')
#   value = models.CharField(max_length= 20, default='1')
#   type = models.CharField(max_length= 20, default='1')
#   path = models.CharField(max_length= 20, default='1')


class Message(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length= 40)
    subject = models.TextField(max_length=14)
    message = models.CharField(max_length=255)
