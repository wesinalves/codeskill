'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue
Initial positions increment by 1 from 1 at the front of the line to n at the back
Any person in the queue can bribe the person directly in front of them to swap positions
If two people swap positions, they still wear the same sticker denoting their original places in line.
One person can bribe at most two others.
the minimum number of bribes that took place to get the queue into its current state!

It must print an integer representing the minimum number of bribes necessary, 
or Too chaotic if the line configuration is not possible. 

###############
Observations
###############

'''
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

