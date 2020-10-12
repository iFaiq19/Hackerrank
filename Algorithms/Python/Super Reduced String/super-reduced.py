#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    i = 0
    strList = list(s)
    while i < len(strList)-1:
        if strList[i] == strList[i+1]:
            del strList[i]
            del strList[i]
            i = 0
        else: 
            i+=1
    if len(strList) == 0: return 'Empty String'
    else: return ''.join(strList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
