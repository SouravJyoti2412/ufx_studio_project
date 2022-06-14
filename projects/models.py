from http import client
from pyexpat import model
from django.db import models
from autoslug import AutoSlugField

class product_catagory(models.Model):
    catagory_name = models.CharField(max_length=30)
    catagory_id = models.CharField(max_length=30)

    def __str__(self):
        return  self.catagory_name


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_shot_des_in_100_word = models.TextField(max_length=100)
    slot1_900x800px = models.FileField(upload_to='project_images/') 
    slot2_900x800px = models.FileField(upload_to='project_images/')
    slot3_900x800px = models.FileField(upload_to='project_images/')
    about_project = models.TextField()
    date = models.DateField()
    client_name = models.CharField(max_length=50)
    url_do_not_use_http = models.CharField(max_length=255,null=True)

    banner_img_2400x1640px = models.FileField(upload_to='project_images/')
    Left_up_image_960x640px = models.FileField(upload_to='project_images/')
    left_down_image_960x640px= models.FileField(upload_to='project_images/') 
    right_up_image_960x640px= models.FileField(upload_to='project_images/')
    right_down_image_960x640px= models.FileField(upload_to='project_images/')
    title_slug = AutoSlugField(populate_from='project_name',unique=True,null=True,default=None)
    # catagory_name = models.ForeignKey(product_catagory, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return  self.project_name 

    

