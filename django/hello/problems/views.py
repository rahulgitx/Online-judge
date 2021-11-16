from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage
import subprocess

def runcppproblem1():
    subprocess.run('rm newfile', shell=True)
    subprocess.run('rm newfile.o', shell=True)
    subprocess.run('touch /onlinejudge/Online-judge/django/hello/compilationoutput.txt', shell=True)
    p = subprocess.run('g++ -c /onlinejudge/Online-judge/django/hello/media/newfile.cpp 2> /onlinejudge/Online-judge/django/hello/errorfile.txt', shell=True)

    subprocess.run('g++ newfile.o -o newfile', shell=True)
    # subprocess.run('echo 5 3 | ./newfile > /onlinejudge/Online-judge/django/hello/media/testcase1.txt', shell=True)  #testcase 1
    subprocess.run('echo -e "Output: \ntest case 1: " | cat > /onlinejudge/Online-judge/django/hello/compilationoutput.txt', shell=True)
    subprocess.run('echo 5 1 2 3 -2 5 | ./newfile >> /onlinejudge/Online-judge/django/hello/compilationoutput.txt', shell=True)  #testcase 1

    subprocess.run('echo -e "\ntest case 2:" | cat >> /onlinejudge/Online-judge/django/hello/compilationoutput.txt', shell=True)
    subprocess.run('echo 4 -1 -2 -3 -4 | ./newfile >> /onlinejudge/Online-judge/django/hello/compilationoutput.txt', shell=True)  #testcase 2

    #comparing the files
    # subprocess.run('x=0')
    # ret=subprocess.run('cmp compilationoutput.txt /onlinejudge/Online-judge/django/hello/static/answerproblem1.txt || echo 1 > ret', shell=True)
    # print("ret returncode: ", ret.returncode)
    # if(ret.returncode == 0):
    #     subprocess.run('echo -e "\nTest cases passed successfully!" >> compilationoutput.txt', shell=True)
    # else:
    #     subprocess.run('echo -e "\nWrong Answer!" >> compilationoutput.txt',shell=True)
    subprocess.run('mv compilationoutput.txt /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt', shell=True)
    subprocess.run('./comparefile.sh', shell=True)
    print('compared!')

    if(p.returncode != 0):
        subprocess.run('cp /onlinejudge/Online-judge/django/hello/errorfile.txt /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt', shell=True)
        subprocess.run('echo compilation error! | cat >> /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt', shell=True)
        print('Compilation error')
        subprocess.run('cat /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt', shell=True)

    # subprocess.run('mv compilationoutput.txt /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt', shell=True)


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
        response = redirect('/static/outputproblem1.txt')
        return response
    return render(request, 'problem1.html')

def submitproblem1(request):
    return render(request, 'submitproblem1.html')

# Create your views here.
