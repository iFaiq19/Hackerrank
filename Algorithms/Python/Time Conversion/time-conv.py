#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[8:] == 'PM' or (s[:2] == '12' and s[8:]== 'AM'):
        a = s[:2]
        a = int(a)
        if a == 12:
            if s[8:] == 'AM':
                a = '00'
            elif s[8:] == 'PM': 
                a = '12'
        else:
            a = a + 12
            a = str(a)
        b = a + s[2:8]
        
    else:
        b = s[:8]
    return str(b)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
