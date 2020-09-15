'''
Code for google kickstart 2017
Round A - Square Counting
Wesin Ribeiro

##############
Problem
##############
find as many different squares as possible
on an evenly spaced rectangular grid of dots
identify four dots that form the vertices of a square
Each side of the square must have the same length, of course
but it does not matter what that length is
the square does not necessarily need to be aligned 
with the axes of the grid
Two squares are different if and only if 
their sets of four dots are different.

given a grid with R rows and C columns of dots
How many different squares can he find in this grid
please output the answer modulo 10^9 + 7 (1000000007).



##############
Comments
##############
how to identify four dots?
min square is 2x2
max square is RxC if C == R, RxC-M, if C > R, R-MxC, if C<R.
total vertices is rxc / 2x2


'''
def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        rc = int(input())
                 
        print('Case #{}: {}'.format(t+1, ans))

main()