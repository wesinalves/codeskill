'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
You are given an unordered array consisting of consecutive integers without any duplicates.
You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the array in ascending order.

arr = [7, 1, 3, 2, 4, 5, 6]

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]



###############
Observations
###############

## brute force solution
make all possibilities of swap combinations and choose the one with minimum number

## insights after test cases
given first element unordered, 
while elements is not ordered 
    swap by his original position
    count the swap


'''

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # check the first unordered
    swaps = 0
    for i,v in enumerate(arr):
        if v != (i+1):
            while v != (i+1):
                # make swap
                arr[i],arr[v-1] = arr[v-1],arr[i]
                v = arr[i]
                swaps += 1
        else:
            continue
    
    print(swaps)

def main():
    t = 2

    for i in range(t):    
        n = int(input())
        c = list(map(int, input().rstrip().split()))
        minimumSwaps(c)
        
main()