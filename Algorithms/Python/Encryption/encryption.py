#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n=len(s)
    row=round(math.sqrt(n))
    row=int(row)
    col=0
    if row>=math.sqrt(n):
        col=row
    else:
        col=row+1
    ans=[]
    for i in range(col):
        j=i
        word=""
        while j<n:
            word=word+s[j]
            if col>row:
                j+=row+1
            else:
                j+=row
        ans.append(word)
    return ' '.join(ans)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
