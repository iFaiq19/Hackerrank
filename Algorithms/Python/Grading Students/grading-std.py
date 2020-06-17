#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    list1 = []
    for i in grades:
        a = i
        b = i+1
        c = i+2
        if i>37:
            if a%5==0:
                list1.append(str(a))
            elif b%5==0:
                list1.append(str(b))
            elif c%5==0:
                list1.append(str(c))
            else:
                list1.append(str(i))
        else:
            list1.append(str(i))
    return(list1)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
