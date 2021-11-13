from django.shortcuts import render, HttpResponse

def problem1(request):
    return render(request, 'problem1.html')

def submitproblem1(request):
    return render(request, 'submitproblem1.html')

# Create your views here.
