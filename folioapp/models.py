
from django.db import models

class contact(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    subject = models.CharField('Subject', max_length=50)
    message = models.CharField('Message', max_length=50)
    
# Create your models here.
