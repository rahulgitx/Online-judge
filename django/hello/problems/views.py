from django.shortcuts import render, HttpResponse

def problem1(request):
    if(request.method == "POST"):
        uploaded_file = request.FILES['userfile']
        print(uploaded_file.name)
        print(uploaded_file.size)
        uploaded_file.read()
    return render(request, 'problem1.html')

def submitproblem1(request):
    return render(request, 'submitproblem1.html')

# Create your views here.
