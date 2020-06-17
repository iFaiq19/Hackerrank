#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    a = z - y
    if a < 0:
        a = a*-1
    b = z - x
    if b < 0:
        b = b*-1
    if a > b:
        return 'Cat A'
    elif a < b:
        return 'Cat B'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
