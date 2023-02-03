#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    counter = 0
    for x in range(len(a)):
        for y in range(0, len(a) - x - 1):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]
                counter += 1
    print('Array is sorted in {:d} swaps.'.format(counter))
    print('First Element: {:d}'.format(a[0]))
    print('Last Element: {:d}'.format(a[len(a) - 1]))
    return
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
