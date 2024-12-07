from django.shortcuts import render

# Create your views here.

def Base(request):
    return render(request,'Base.html')

def Home(request):
    return render(request,'Home.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def Login(request):
    return render(request, 'Login.html')

def Carousel(request):
    return render(request,'Carousel.html')

def Navbar(request):
    return render(request,'Navbar.html')

def Footer(request):
    return render(request,'Footer.html')

def FAQ(request):
    return render(request,'FAQ.html')