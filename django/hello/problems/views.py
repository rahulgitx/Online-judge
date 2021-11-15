from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import subprocess

def runcpp():
    subprocess.run('rm newfile', shell=True)
    subprocess.run('rm newfile.o', shell=True)
    subprocess.run('g++ -c /onlinejudge/Online-judge/django/hello/media/newfile.cpp', shell=True)
    subprocess.run('g++ newfile.o -o newfile', shell=True)
    subprocess.run('./newfile > /onlinejudge/Online-judge/django/hello/media/outputfile.txt', shell=True)
    print()
    print("g++ command ran successfully")


def problem1(request):
    if(request.method == "POST"):
        uploaded_file = request.FILES['userfile']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        # uploaded_file.read()
        subprocess.run('rm /onlinejudge/Online-judge/django/hello/media/*', shell=True)
        fs = FileSystemStorage()
        uploaded_file.name = "newfile.cpp"                       # changing the name of the incoming file
        # print(uploaded_file.name," ", uploaded_file)
        fs.save(uploaded_file.name, uploaded_file)
        runcpp()
    return render(request, 'problem1.html')

def submitproblem1(request):
    return render(request, 'submitproblem1.html')

# Create your views here.
