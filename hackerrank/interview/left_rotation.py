'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
A left rotation operation on an array shifts each of the array's elements
1 unit to the left.
Given an array a of n intergers and a number d, perform d left rotations 
on the array. Return the updated array to be printed as a single line of space-separated integers.

###############
Observations
###############

1 <= n <= 10**5
1 <= d <= n
1 <= a[i] <= 10**6

'''

import math
import os
import random
import re
import sys

def left_rotaion(array):
    array_0 = array.pop(0)
    array.append(array_0)

def rotleft(array, rotations):
    for _ in range(rotations):
        left_rotaion(array)
    return array

def main():
    t = 2

    for i in range(t):    
        n, d = list(map(int, input().rstrip().split()))
        a = list(map(int, input().rstrip().split()))
        result = rotleft(a, d)
        result = ' '.join(map(str, result))
        print('Case #{}: {}'.format(i+1, result))

main()