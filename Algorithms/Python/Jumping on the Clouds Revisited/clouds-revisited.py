#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    j = 0
    for i in range(0,e,k):
        j = (i+k)%len(c)
        if j!=0:
            if c[j]==1:
                e -= 3
            elif c[j]==0:
                e-=1
        else:
            if c[j]==1:
                e -= 3
            else:
                e-=1
            break
        print(e)
    return e



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
