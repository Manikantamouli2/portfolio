from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def About(request):
    return render(request,'About.html')

def experience(request):
    experience=[
        {"company":"Symbiosis Technologies",
        "position":"python developer"},
        {"company":"Namoona 3D Labs",
        "position":"Back end Developer"},
        {"company":"Eduskills",
        "position":"Full Stack DEveloper"}
    ]
    return render (request,"experience.html",{"experience":experience})
def certifications(request):
    return render(request,"certifications.html")
def contact(request):
    return render(request,'contact.html')
def resume(request):
    return render(request,'resume.html')

    