from django.db import models


#Model 1
class Account(models.Model):
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=120)
    repassword = models.CharField(max_length=120)

#Model 2 
class Personal_Details(models.Model):
    title_face = models.CharField(max_length=120, default=True)
    image_face = models.ImageField(upload_to='media')
    title_ID = models.CharField(max_length=120, default=True)
    image_ID = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title_face, self.title_ID
