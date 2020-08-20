#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def absolute_difference(a, b):
    return abs(a - b)

def diagonalDifference(arr):
    # Write your code here
    primary_sum = sum([arr[i][i] for i in range(len(arr))])
    secondary_sum = sum([arr[i][-i-1] for i in range(len(arr))])
    
    return absolute_difference(secondary_sum, primary_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
