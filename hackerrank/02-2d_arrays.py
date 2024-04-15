#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    hourglass = []
    top_down = [[-1,-1],[-1,0],[-1,1]]
    
    for row in range(1,len(arr)-1): # rows
        for column in range(1,len(arr[0])-1): # columns
            sum_hour = 0
            sum_hour += arr[row][column]
            for factor in top_down:
                sum_hour += (arr[row+factor[0]][column+factor[1]] + arr[row-factor[0]][column+factor[1]])
            hourglass.append(sum_hour)
    return max(hourglass)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
