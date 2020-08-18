'''
n -> stacks
k -> plates
p -> chosen plate
'''

T = int(input())
N,K,P = 0,0,0
PREFIX = []
VALUES = []
CACHE = []

def precompute_sum(matrix_values, num_stacks, num_plates):
    '''Precompute sum of first x plates from stack i'''
    sum_of_firsts = []
    for st in range(num_stacks):
        sum_in_stack = []
        for p in range(1, num_plates + 1):
            sum_in_stack.append(sum(matrix_values[st][:p]))
        sum_of_firsts.append(sum_in_stack)
    #print(sum_of_firsts)
    return sum_of_firsts


def beuty(idx, plate):
    '''Recursive function to find max solution'''
    print(idx, plate)
    if plate == P:
        return 0
    if idx >= N or plate >= P:
        return -1e9
    if CACHE[idx][plate] != -1:
        return CACHE[idx][plate]
    ans = -1e9
    for i in range(K):
        ans = max(ans, PREFIX[idx][i] + beuty(idx+1, plate+i))
    CACHE[idx][plate] = ans
    
    return ans

for t in range(T):
    VALUES = []
    CACHE = []
    N,K,P = list(map(int, input().split()))
    CACHE = [[-1 for _ in range(P)] for _ in range(N)]
    for _ in range(N):
        VALUES.append(list(map(int, input().split())))
    print(N,K,P)
    PREFIX = precompute_sum(VALUES, N, K)
    maximum = beuty(0, 0)
    print('Case #{}: {}'.format(t+1, maximum))
