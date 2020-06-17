#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color = {}
    count = 0
    for pair in ar:
        if pair not in color:
            color[pair] = 0
        color[pair] += 1
    for i in color:
        if color[i] >1:
            count += color[i]//2
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
