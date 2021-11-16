#!/bin/bash
# x=0
# # cmp --silent --  /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt /onlinejudge/Online-judge/django/hello/static/answerproblem1.txt || echo -e "\nWrong answer    !" >> /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt
# echo $x
if cmp --silent --  /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt /onlinejudge/Online-judge/django/hello/static/answerproblem1.txt 
then echo -e "\nTest cases passed Successfully!" >> /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt
else
echo -e "\nWrong Answer!" >> /onlinejudge/Online-judge/django/hello/static/outputproblem1.txt
fi