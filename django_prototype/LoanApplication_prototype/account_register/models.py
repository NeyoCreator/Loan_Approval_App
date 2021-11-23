from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=120)
    repassword = models.CharField(max_length=120)