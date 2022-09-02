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
    temp = arr[n - 1]
    if arr[0] >= temp:
        for x in range(n - 1, 0 , -1):
            arr[x] = arr[x - 1]
            for y in range(len(arr)):
                print(arr[y], end = ' ')
            print()
        arr[0] = temp
        for ab in range(n):
            print(arr[ab], end = ' ')
        print()
    else:
        for x in range(n - 1 , -1, -1):
            if arr[x] >= temp and arr[x - 1] < temp:
                pass
            elif arr[x] >= temp:
                arr[x] = arr[x - 1]
                for y in range(len(arr)):
                    print(arr[y], end = ' ')
                print()
            elif arr[x] < temp:
                arr[x + 1] = temp
                
                for y in range(len(arr)):
                    print(arr[y], end = ' ')
                print()
                break
    return
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
