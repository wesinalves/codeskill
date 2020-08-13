'''
Code for google kickstart
Round C - Countdown
Wesin Ribeiro
2020

##############
Observations
##############
By the size of inputs
the solution must have time complexity equals to 0(N).
The solution is very sofisticated way to find K-countdowns in linear time.
We need just one loop to find the number of countdowns.
The secret is using a flag which has initial value equals to -1.
Everytime the actual valeu of array is equal to K, we set the flag to K that is the begining of our countdown.
Thus, we decrement our flag and compare with the next element of the input. If they are equal we decrement again, otherwise we set flag to -1.
Once we are decrementing the flag, when it is equal to zero, it means that we find the K-countdown, then increment a variable count.
The process will continue until the end of input
'''

def countdown(vet, length, start):
    '''Return Countdowns'''
    count = 0
    flag = -1
    for i in range(length):
        if vet[i] == start:
            flag = start

        if vet[i] == flag:
            flag -= 1
        else:
            flag = -1

        if flag == 0:
            count += 1

    return count

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        n, k = list(map(int, input().split()))
        samples = list(map(int, input().split()))
        ans = countdown(samples, n, k)
        print('Case #{}: {}'.format(t+1, ans))

main()