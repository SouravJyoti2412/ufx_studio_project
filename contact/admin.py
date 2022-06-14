from django.contrib import admin
from contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','email','option_field','massage')
    model = Contact
    list_per_page = 5

admin.site.register(Contact,ContactAdmin)
# Register your models here.

