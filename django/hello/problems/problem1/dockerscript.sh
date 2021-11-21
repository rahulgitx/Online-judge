#!/bin/bash

# touch compilationoutputfile.txt
touch errorfile.txt
g++ -c newfile.cpp 2> errorfile.txt
g++ newfile.o -o newfile

echo -e "Output: \ntest case 1: " | cat > compilationoutput.txt
echo 5 1 2 3 -2 5 | timeout -k 0 1 ./newfile >> compilationoutput.txt
echo -e "\ntest case 2:" | cat >> /compilationoutput.txt
echo 4 -1 -2 -3 -4 | timeout -k 0 1 ./newfile >> /compilationoutput.txt

if [ $? -ne 0 ]
# then echo Time Limit Exceeded!! | cat > compilationoutput.txt
then x=0                     #stored this for later
else x=1 
fi

if cmp --silent --  compilationoutput.txt answerproblem1.txt 
then echo -e "\nTest cases passed Successfully!" >> compilationoutput.txt
else
echo -e "\nWrong Answer!" >> compilationoutput.txt
fi

if [ $x == 0 ]
then echo Time Limit Exceeded!! | cat > compilationoutput.txt               #will append over the last wrong answer.
fi

if [ -s errorfile.txt ]
then
cp errorfile.txt compilationoutput.txt  #non empty
echo Compilation error! | cat >> compilationoutput.txt
fi
