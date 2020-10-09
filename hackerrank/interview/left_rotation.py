'''
Code for HackerRank
Interview Preparation Kit
Wesin Ribeiro

###############
problem
###############


###############
Observations
###############


'''

def left_rotaion(array):
    pass

def main():
    t = 2

    for i in range(t):    
        n = int(input())
        c = list(map(int, input().rstrip().split()))
        result = left_rotaion(c)
        print('Case #{}: {}'.format(i+1, result))

main()