#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    lst = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]==a[j]:
                b = j-i
                lst.append(b)
    if lst != []:
        return min(lst)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
