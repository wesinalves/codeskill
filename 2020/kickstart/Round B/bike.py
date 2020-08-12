'''
Code for google kickstart
Round B - Bike Tour
Wesin Ribeiro
2020
'''

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        n = int(input())
        checkpoints = list(map(int, input().split()))
        peaks = 0
        for i in range(1, n-1):
            if checkpoints[i-1] < checkpoints[i] > checkpoints[i+1]:
                peaks += 1

        print('Case #{}: {}'.format(t+1, peaks))

main()
