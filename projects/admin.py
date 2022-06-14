from django.contrib import admin

# Register your models here.

from projects.models import Project,product_catagory


admin.site.register(Project)
admin.site.register(product_catagory)