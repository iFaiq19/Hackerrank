#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if len(s)+len(t)<k:
        return 'Yes'
    sameChar = 0
    for i,j in zip(s, t):
        if i == j:
            sameChar += 1
        else: break
    diff = (len(s)-sameChar)+(len(t)-sameChar)
    if diff <= k and (diff-k)%2 == 0:
        return 'Yes'
    else: return 'No'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
