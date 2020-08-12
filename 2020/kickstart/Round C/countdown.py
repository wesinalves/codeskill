'''
Code for google kickstart
Round C - Countdown
Wesin Ribeiro
2020
'''
def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        n, k = list(map(int, input().split()))
        samples = list(map(int, input().split()))
        print('Case #{}: {}'.format(t+1, ans))

main()