'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############
string s repeated infinitely many times.
find and print the number of letter a's in the first n given integer
1 <= s <= 100
1 <= n <= 10**12
for 25%, 1 <= n <= 10**6

###############
Observations
###############
It counts the number of "a" in a full string, and in the last, 
potentially partial string, and calculates the total amount of "a" based on that.
"a" count of full string * number of string repeats + "a" count of last string.
'''

def repeatedString(s, n):
    num_base = s.count('a')
    rest = n % len(s)
    num_rest = s[:rest].count('a')    
    return num_base * (n // len(s)) + num_rest

def main():
    t = 2

    for i in range(t):    
        n = int(input())
        c = list(map(int, input().rstrip().split()))
        result = repeatedString(c)
        print('Case #{}: {}'.format(i+1, result))

main()