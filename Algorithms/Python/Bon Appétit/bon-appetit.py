#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum = 0
    anna = 0
    retur = 0
    for i in bill:
        sum += i
    sum = sum/2
    for j in range(len(bill)):
        if j == k:
            continue
        else:
            anna += bill[j]
    anna = anna/2
    retur = b - anna
    retur = int(retur)
    if retur != 0:
        print(retur)
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
