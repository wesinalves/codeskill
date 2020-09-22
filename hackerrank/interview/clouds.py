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
###############
Observations
###############
Try to jump 2 clouds, if not a good choice jump 1.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    pointer = 0
    jumps = 0
    while pointer < len(c):
        try:
            if c[pointer + 2] == 0:
                jumps += 1
                pointer += 2
            else:
                jumps += 1
                pointer += 1
        except:
            if pointer == len(c) - 2:
                jumps += 1
            break
    
    return jumps


def main():
    t = 2

    for i in range(t):    
        n = int(input())
        c = list(map(int, input().rstrip().split()))
        result = jumpingOnClouds(c)
        print('Case #{}: {}'.format(i+1, result))

main()