#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    a = str(i)
    a = a[::-1]
    b = int(a)
    count = 0
    ls = []
    for i in range(i, j+1):
        a = str(i)
        a = a[::-1]
        b = int(a)
        if (i-b) < 0:
            c = -1*(i-b)
            ls.append(c)
        else:
            c = i-b
            ls.append(c)
    for i in ls:
        if i % k == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
