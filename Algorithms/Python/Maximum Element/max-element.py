#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    maxStack = [0]
    printMax = []
    for i in range(len(operations)):
        temp = list(map(int, operations[i].split(' ')))
        if temp[0] == 1:
            stack.append(temp[1])
            if temp[1] >= maxStack[-1]:
                maxStack.append(temp[1])
        elif temp[0] == 2:
            if stack.pop() == maxStack[-1]:
                maxStack.pop()
        else:
            printMax.append(maxStack[-1])
    return printMax

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
