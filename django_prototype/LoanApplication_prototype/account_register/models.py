from django.db import models


#Model 1
class Account(models.Model):
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=120)
    repassword = models.CharField(max_length=120)

#Model 2 
class Personal_Details(models.Model):
    title = models.CharField(max_length=120, default=True)
    image = models.ImageField(upload_to='media')
    #Extracted text
    def __str__(self):
        return self.title
