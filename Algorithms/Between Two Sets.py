#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def is_factor(number, factor):
    return number % factor == 0

def multiple_of_a(a, multiple):
    for i in a:
        if multiple % i != 0:
            return False
    return True

def factor_of_b(b, factor):
    for i in b:
        if i % factor != 0:
            return False
    return True



def getTotalX(a, b):
    # Write your code here
    max_a = max(a)
    min_b = min(b)
    count = 0

    for i in range(max_a, min_b+1, max_a):
        print("trying i =", i)
        if multiple_of_a(a, i) and factor_of_b(b, i):
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
