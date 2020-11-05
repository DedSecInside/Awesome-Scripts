#Author: @ankitRai96
#Purpose: to find duplicate files
#Input: paths of two (seperate) directories
#Output: Name of files which are common

import os

def FindDuplicateFile(f1, f2):
    """
    Search files in f1.

    Args:
        f1: (todo): write your description
        f2: (todo): write your description
    """
    f1content = os.listdir(f1)
    f2content = os.listdir(f2)

    #let's compare (naive approach)
    for item in f1content:
        for check in f2content:
            if item == check:
                print(item)
    
if __name__ == '__main__':
    d1 = input("Enter path of First Folder: ")
    d2 = input("Enter path of Second Folder: ")
    FindDuplicateFile(d1,d2)