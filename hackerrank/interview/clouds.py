'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
Some of the clouds are thunderheads and others are cumulus
She can jump on any cumulus cloud having a number that is equal to the 
number of the current cloud plus  1 or 2.
She must avoid the thunderheads. Determine the minimum number of jumps 
it will take Emma to jump from her starting postion to the last cloud. 
It is always possible to win the game. 
Complete the jumpingOnClouds function in the editor below. 
It should return the minimum number of jumps required, as an integer. 
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
