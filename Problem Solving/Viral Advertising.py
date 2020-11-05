#!/bin/python

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    """
    Calculate the number of viral.

    Args:
        n: (todo): write your description
    """

    count = 0
    start = 5
    for i in range(0,n):
        count =count + start/2
        start = (start/2)*3

    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

