from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import subprocess

def runcppproblem1():
    subprocess.run('rm newfile', shell=True)
    subprocess.run('rm newfile.o', shell=True)
    subprocess.run('g++ -c /onlinejudge/Online-judge/django/hello/media/newfile.cpp', shell=True)
    subprocess.run('g++ newfile.o -o newfile', shell=True)
    p = subprocess.run('echo 5 3 | ./newfile > /onlinejudge/Online-judge/django/hello/media/testcase1.txt', shell=True)  #testcase 1
    if(p.returncode != 0):
        print('Compilation error!')
    # subprocess.run('echo 5 1 2 3 -2 5 | ./newfile > /onlinejudge/Online-judge/django/hello/media/testcase1.txt', shell=True)  #testcase 1
    # subprocess.run('echo 4 -1 -2 -3 -4 | ./newfile > /onlinejudge/Online-judge/django/hello/media/testcase2.txt', shell=True)  #testcase 2
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
        runcppproblem1()
    return render(request, 'problem1.html')

def submitproblem1(request):
    return render(request, 'submitproblem1.html')

# Create your views here.
