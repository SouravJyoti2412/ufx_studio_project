from django.db import models

class Clint_compny_logo(models.Model):
    
    Comapany_logo = models.ImageField(upload_to='brands/', height_field=None, width_field=None, max_length=100)
    


    
