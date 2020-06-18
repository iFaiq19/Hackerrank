#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    num = "0123456789"
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char = "!@#$%^&*()-+"
    count=0
    dict = {'num':0, 'up':0,'low':0,'char':0}
    if n<=6:
        return 6 - n
    else:
        for i in range(n):
            if password[i] in num:
                dict['num'] += 1
            elif password[i] in low:
                dict['low'] += 1
            elif password[i] in up:
                dict['up'] += 1
            else:
                dict['char'] += 1
        for i in dict:
            if dict[i] == 0:
                count += 1
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
