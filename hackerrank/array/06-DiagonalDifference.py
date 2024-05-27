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

def diagonalDifference(arr):
    i_point = 0
    lr_diagonal = 0
    j_point = -1
    rl_diagonal = 0
    
    for i in range(len(arr)):
        lr_diagonal += arr[i][i_point]
        rl_diagonal += arr[i][j_point]
        i_point += 1
        j_point -= 1
    
    return (lr_diagonal - rl_diagonal) if lr_diagonal > rl_diagonal else -(lr_diagonal - rl_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
