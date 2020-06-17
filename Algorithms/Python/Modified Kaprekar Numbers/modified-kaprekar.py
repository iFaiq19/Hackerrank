#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    lst = []
    for i in range(p,q+1):
        a = str(i)
        b = i*i
        b = str(b)
        b = b[::-1]
        if i == 1:
            lst.append(1)
        elif len(b) >= 2:
            c = len(a)
            d = b[:c-1:-1]
            e = b[c-1::-1]
            f = int(d)+int(e)
            if int(f) == int(a):
                lst.append(int(f))
    if lst ==[]:
        print('INVALID RANGE')
    else:
        for i in lst:
            print(i, end=' ')
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
