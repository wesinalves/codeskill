'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
An hourglass in A is a subset of values with indices falling in this pattern
Calculate the hourglass sum for every hourglass in arr then print the maximum hourglass sum. 
The array will always be 6 x 6

###############
Observations
###############

'''

import math
import os
import random
import re
import sys

def sum_pattern(array, row, column):
    pattern = list()
    pattern.append(array[row][column])
    pattern.append(array[row][column + 1])
    pattern.append(array[row][column + 2])

    pattern.append(array[row + 1][column + 1])
    
    pattern.append(array[row + 2][column])
    pattern.append(array[row + 2][column + 1])
    pattern.append(array[row + 2][column + 2])
    return sum(pattern)
# Complete the hourglassSum function below.
def hourglassSum(arr):
    ## initialization
    values = list()
    ## processing
    # find hourglass
    for i in range(4):
        for j in range(4):
            values.append(sum_pattern(arr,i,j)) # sum hourglass values and store
    
    # get max hourglass
    return max(values)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
