from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import subprocess

def problem1(request):
    if(request.method == "POST"):
        uploaded_file = request.FILES['userfile']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        # uploaded_file.read()
        subprocess.run('dir "D:/Algo university/Online judge/Online-judge/django/hello/media"')
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'problem1.html')

def submitproblem1(request):
    return render(request, 'submitproblem1.html')

# Create your views here.
