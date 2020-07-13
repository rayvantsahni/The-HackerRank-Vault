#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    hg_sum = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for j in range(len(arr[:-2])):
        for i in range(len(arr[0][:-2])):
            hg_sum.append(arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2])

    print(max(hg_sum))
