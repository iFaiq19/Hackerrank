#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a = len(arr)
    b1 = 0
    b2 = 0
    b3 = 0
    for i in arr:
        if i > 0:
            b1 += 1
        elif i < 0:
            b2 += 1
        else:
            b3 += 1
    lst = [b1/a, b2/a, b3/a]
    for i in lst:
        i = round(i, 6)
        print(i)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
