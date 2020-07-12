#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = str(bin(n).replace("0b", "")).split("0")
    print(len(max(b)))
