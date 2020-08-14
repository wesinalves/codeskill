'''
Code for google kickstart
Round D - Record Breaker
Wesin Ribeiro
2020
##############
Observations
##############

'''

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        n = int(input().split())
        samples = list(map(int, input().split()))
        print('Case #{}: {}'.format(t+1, ans))

main()