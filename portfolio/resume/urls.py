
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("About/",views.About,name="About"),
    path("experience/",views.experience,name="experience"),
    path("certifications/",views.certifications,name="certifications"),
    path("contact/",views.contact,name="contact"),
    path("resume/",views.resume,name="resume")
]

