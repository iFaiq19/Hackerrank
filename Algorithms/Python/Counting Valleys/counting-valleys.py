#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ans = 0
    count = 0
    for i in range(n):
        if s[i] == 'D':
            count -=1
        else:
            count +=1
        if s[i] == 'U' and count == 0:
            ans +=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
