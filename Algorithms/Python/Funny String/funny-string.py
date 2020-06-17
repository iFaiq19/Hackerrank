#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rs = s[::-1]
    n = len(s)
    for i in range(1, n):
        d1 = ord(s[i]) - ord(s[i - 1])
        d2 = ord(rs[i]) - ord(rs[i - 1])
        if d1 == d2 or -1*(d1)==d2 or d1==-1*(d2):
            x = "Funny"
        else:
            x = "Not Funny"
            break
    return x



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
