from django.db import models

class CareerRegister(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=30)
    contact_no = models.BigIntegerField()
    email = models.EmailField( max_length=254)
    document = models.FileField(upload_to='cv/')
    Experinace = models.CharField(max_length=2)  

    skill = models.CharField(max_length=50)
    job_profile = models.CharField(max_length=30)
    address = models.TextField()

   
    
is_active = models.BooleanField(default=False)
 