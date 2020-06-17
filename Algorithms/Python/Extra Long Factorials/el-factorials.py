#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    a = 1
    for i in range(n, 0, -1):
        a *= i
    print(a)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
