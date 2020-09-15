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
        previous = 0
        n = int(input())
        samples = list(map(int, input().split()))
        for i in range(n):
            greater_than_previous = (i == 0 or samples[i] > previous)
            greater_than_following = (i == n-1 or samples[i] > samples[i + 1])
            if greater_than_previous and greater_than_following:
                ans += 1
            
            previous = max(previous, samples[i])

        print('Case #{}: {}'.format(t+1, ans))

main()