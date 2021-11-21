from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage
import subprocess
import problems.problem1.problem1


def problem1func(request):
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
        # runcppproblem1()
        # rundockerproblem1()
        problems.problem1.problem1.rundockerproblem1()
        print("back from docker ")
        # response = redirect('/static/outputproblem1.txt')
        # response = redirect('/static/answerproblem1.txt')
        # return response
        return HttpResponseRedirect('/static/outputproblem.txt')
    return render(request, 'problem1.html')

def submitproblem1(request):                #not in use
    return render(request, 'submitproblem1.html')

# Create your views here.
