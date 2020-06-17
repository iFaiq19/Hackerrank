#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    min = 0
    max = 0
    for i in range(len(arr)-1):
        min += arr[i]
    for j in range(1, len(arr)):
        max += arr[j]
    print(min, max) 

        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
