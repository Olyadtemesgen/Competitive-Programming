#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    end =arr[-1]
    length = len(arr) - 2
    while length + 1 and arr[length] > end:
        arr[length + 1] = arr[length] 
        print(" ".join(list(map(str, arr))))
        length -= 1
    arr[length + 1] = end
    print(" ".join(list(map(str, arr))))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
