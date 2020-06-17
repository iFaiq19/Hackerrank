#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    ascii = []
    for i in s:
        slow = i.lower()
        ascii.append(ord(slow))
    for i in range(97,123):
        if i not in ascii:
            return 'not pangram'
            break
    else:
        return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
