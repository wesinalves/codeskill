'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
An avid hiker keeps meticulous records of their hikes. During the last hike that 
took exactly steps steps, for every step it was noted if it was an uphill, U, 
or a downhill, D step. Hikes always start and end at sea level, 
and each step up or down represents a 1 unit change in altitude. 
We define the following terms:
    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 
################
observations
################
everytime D occours above sea level
trigging a flag , when return to sea level count the value
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valley_flag = False
    count = 0
    for p in path:
        if p == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        if sea_level < 0:
            valley_flag = True
        elif sea_level == 0 and valley_flag == True:
            count += 1
            valley_flag = False 
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
