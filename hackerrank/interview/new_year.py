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

* initial state is the ascending sorted line 
* if the current position is larger than two, so it is chaotic
* how to count the number of bribes?

my first approach is counting the number of bubbles in bubble sort algorithm,
but this solution doesn't work for large list of numbers,
even if I break the counting when I realize that the list is chaotic.

who far is a element from initial position?
if distance > 2, list is too chaotic
else, sum the distances.

we don't care if P has moved
forwards, it is better to count how many times
P has RECEIVED a bribe, by looking at who is
ahead of P.  P's original position is the value
of P.

Anyone who bribed P cannot get to higher than
one position in front if P's original position,
so we need to look from one position in front
of P's original position to one in front of P's
current position, and see how many of those 
positions in Q contain a number large than P.

In other words we will look from P-1 to i-1,
which in Python is range(P-1,i-1+1), or simply
range(P-1,i).  To make sure we don't try an
index less than zero, replace P-1 with
max(P-1,0)

'''
import math
import os
import random
import re
import sys

# # Complete the minimumBribes function below.
# def minimumBribes(q):
#     length = len(q)
#     bribe = 0
#     for i in range(length):
#         swap = 0
#         for j in range(length - i - 1):            
#             if q[j] > q[j+1]:
#                 q[j], q[j+1] = q[j+1], q[j]
#                 swap += 1
#                 bribe += 1
#             if swap > 2:            
#                 break
#         if swap > 2:            
#                 break
        
#     if swap > 2:
#         print('Too chaotic')
#     else:
#         print(bribe)

def minimumBribes(q):
    length = len(q)
    bribe = 0
    distance = 0
    for i,p in enumerate(q):
        print(i,p)
        distance = p - (i+1)
        if distance > 2:
            print('Too chaotic')
            return
        for j in range(max(p-2,0),i):
            if q[j] > p:
                bribe += 1
        
    print(bribe)

def main():
    t = 2

    for i in range(t):    
        n = int(input())
        c = list(map(int, input().rstrip().split()))
        minimumBribes(c)
        
main()

