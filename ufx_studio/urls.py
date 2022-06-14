"""ufx_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ufx_studio import views 
from django.conf import settings
from django.conf.urls.static import static
from ufx_studio.settings import MEDIA_ROOT

admin.site.site_header = "Login to admin panel "
admin.site.site_title = "welcome to Ufx Studio dashboard"
admin.site.index_title ="Ufx Studio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name = "home"),
    path('about/', views.about , name="about") ,
    path('career/', views.career , name = "career"),
    path('contact/', views.contact , name= "contact"),
    path('project_details/<slug>', views.project_details , name = "project_details"),
    path('services/', views.services, name = "services"),
    path('testimonials/', views.testimonials, name = "testimoni"),
    path('allproject/', views.projects , name = "projects"),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)