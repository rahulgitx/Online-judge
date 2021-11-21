import subprocess



def rundockerproblem1():
    # subprocess.run('rm /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt', shell=True)
    subprocess.run('docker run -id --name p1 gcc', shell=True)
    subprocess.run('docker cp /onlinejudge/Online-judge/django/hello/media/newfile.cpp p1:/newfile.cpp', shell=True)
    subprocess.run('docker cp /onlinejudge/Online-judge/django/hello/problems/problem1/dockerscript.sh p1:/dockerscript.sh', shell=True)
    subprocess.run('docker cp /onlinejudge/Online-judge/django/hello/problems/problem1/answerproblem1.txt p1:/answerproblem1.txt', shell=True)
    subprocess.run('docker exec p1 ./dockerscript.sh', shell=True)
    subprocess.run('docker cp p1:/compilationoutput.txt /onlinejudge/Online-judge/django/hello/static/outputproblem.txt', shell=True)
    subprocess.run('docker stop p1', shell=True)
    subprocess.run('docker rm p1', shell=True)
    return  
    
    

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