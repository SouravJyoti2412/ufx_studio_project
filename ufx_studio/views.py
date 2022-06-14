from email.headerregistry import Address
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from contact.models import Contact
from career.models import CareerRegister
from django.contrib import messages
from projects.models import Project 
from django.core.mail import send_mail,EmailMessage
from ourclint.models import Clint_compny_logo



#Start Views Of Home

def home(request):
    projects = Project.objects.all()
    clints = Clint_compny_logo.objects.all()
    return render(request,"home.html",{'projects':projects,'clints':clints})

#End Views Of Home



#Start Views Of About

def about(request):
    return render(request,"about.html")

#end Views Of About


#Start views of Career 

def career(request):
    # cvs = CareerRegister.objects.latest('document')
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        ph_num = request.POST["phone"]
        email = request.POST["email"]
        cv = request.FILES["cv_upload"]
        expererience = request.POST["Experiance_year"]
        skills = request.POST["Skills"]
        job_profile = request.POST["job_profile"]
        Address = request.POST["address"]
        print(name,surname,ph_num,email,cv,expererience,skills,job_profile,Address)
        data = CareerRegister(name=name,lname=surname,contact_no=ph_num,email=email,document=cv,Experinace=expererience,skill=skills,job_profile=job_profile,address=Address)
        data.save()
        messages.success(request,"sucessfully send Your details to recruiter", extra_tags="career")
        email = EmailMessage(
                f'Get email For interview of {name} {surname} ',
                f'Name : {name} {surname} , email id : {email} , phone no : {ph_num} experiance  year :{expererience} ,skill : {skills}, job profile : {job_profile}, address: {Address},',
                '',
               ['astrologertheindian@gmail.com'])
        # email.attach_file(f'H:/django project/ufx_studio/media/cv/{cvs}')
        email.send()
        return redirect('career')
    return render(request,"career.html")


#End views of Career 


#Start views of Contact

def contact(request):
    if request.method == "POST":
        fname = request.POST["name"]
        lname = request.POST["surname"]
        emailid = request.POST["email"]
        optionfiled = request.POST["department"]
        message = request.POST["message"]
        print (fname , lname , emailid , optionfiled , message)
        get_data = Contact( First_name = fname , Last_name=lname , email=emailid , option_field = optionfiled , massage=message )
        get_data.save()
        messages.success(request,"sucessfully send Your message", extra_tags="contact")
        email = EmailMessage(
                f'{fname}" "{lname} contact Us by Conatct page from website',
                f'Name : {fname} {lname } , email id : {emailid} , Depertment : {optionfiled} ,and message : {message} ',
                'souravjoyti@gmail.com',
               ['astrologertheindian@gmail.com'])
        email.send()
        return redirect ( 'contact') 
    return render(request,"contact.html")

#end Views of contact



#start views of Project Details page

def project_details(request, slug):
    projects_details = Project.objects.get(title_slug=slug)
    data ={
        'project_details':projects_details , 
    }
    return render(request,"project_details.html",data)

#end views of Project Details page


#Start views of Services

def services(request):
    return render(request,"services.html")

#End Views of Services


#Start views of Testemonial

def testimonials(request):
    return render(request,"testimonials.html")

#end views of Testemonial


#start views of Projects

def projects(request):
    projects = Project.objects.all()
    return render(request,"projects.html",{'all_project': projects})

#End views of Projects