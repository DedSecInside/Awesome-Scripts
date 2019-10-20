#!/bin/python

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0;
    mylist=[]
    for i in range(i,j+1):
        mylist.append(str(i));

    reverse=[]
    for i in range(0,len(mylist)):
        reverse.append((mylist[i][::-1]))
    
    for i in range(0,len(mylist)):
        print(abs(int(mylist[i])-int(reverse[i])))
        if(abs((int(mylist[i])-int(reverse[i])))%k==0):
            count = count+1;
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = raw_input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

