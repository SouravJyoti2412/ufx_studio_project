from django.contrib import admin

from career.models import CareerRegister


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','lname','contact_no','email','document','Experinace','skill','job_profile','address')
    model = CareerRegister
    list_per_page = 5
admin.site.register(CareerRegister,UserAdmin)
