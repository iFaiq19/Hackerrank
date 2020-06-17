#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    coun1 = 0
    coun2 = 0
    b = []
    for i in scores:
        if i > max:
            max = i
            coun1 += 1
        elif i < min:
            min = i
            coun2 += 1
    b.append(str(coun1))
    b.append(str(coun2))
    return b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
