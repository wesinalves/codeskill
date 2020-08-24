'''
Code for google kickstart
Round E - Longest Arithmetic
Wesin Ribeiro
2020

##############
Problem
##############
An arithmetic array is an array that contains at least two integers
and the differences between consecutive integers are equal.

help to determine the length of the longest contiguous arithmetic subarray
given a array.

##############
Comments
##############
It seems a DP problem
a brute force solution is loop for each element and test if has size grather
than 2 and the next element are consecutive.

'''

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        n = int(input())

        print('Case #{}: {}'.format(t+1, ans))

main()