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
        n = int(input())
        samples = list(map(int, input().split()))
        for i in range(1, n-1):
            if samples[i] > samples[i+1] and samples[i] > samples[i-1]):
                print(samples[i], samples[i-1], samples[i+1])
                ans += 1



        print('Case #{}: {}'.format(t+1, ans))

main()