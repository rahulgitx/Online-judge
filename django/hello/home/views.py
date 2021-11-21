from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contacts
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {
        'variable1':'Joe',
        'variable2':'kelly'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page!")

def about(request):
    return render(request, 'about.html')
#     return HttpResponse("This is about page!")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contacts(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
    return render(request, 'contacts.html')
    # return HttpResponse("This is contacts page")


def index(request):
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            #authenticate
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return render(request, 'index.html')