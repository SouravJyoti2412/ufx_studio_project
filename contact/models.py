from tkinter import YES
from tkinter.messagebox import NO
from django.db import models

class Contact(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    option_field = models.CharField(max_length=50)
    massage = models.TextField(default=NO)
