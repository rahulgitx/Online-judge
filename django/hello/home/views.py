from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home page!")

def about(request):
    return HttpResponse("This is about page!")

def services(request):
    return HttpResponse("This is services page")

def contacts(request):
    return HttpResponse("This is contacts page")