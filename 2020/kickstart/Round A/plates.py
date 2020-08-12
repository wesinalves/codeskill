'''
n -> stacks
k -> plates
p -> chosen plate
'''

cases = int(input())

'''
def precompute_sum(matrix_values, num_stacks, num_plates, plates):
    '''Precompute sum of first x plates from stack i'''
    sum_of_firsts = []
    for i in range(num_stacks):
        sum_in_stack = []
        for p in range(1, num_plates + 1):
            sum_in_stack.append(sum(matrix_values[i][:p]))
        sum_of_firsts.append(sum_in_stack)
    #print(sum_of_firsts)
    return sum_of_firsts


def max_solution(matrix_values, num_stacks, num_plates, plates):
    '''Take all possible solution for P plates'''
    solution = [[0 for _ in range(plates)] for _ in range(num_stacks)]
    summation = precompute_sum(matrix_values, num_stacks, num_plates, plates)
    solution[0][1:] = summation[0]
    for i in range(1, num_stacks):
        for j in range(plates):
            solution[i][j] = 0
            for x in range(min(j, num_plates)):
                solution[i][j] = max(solution[i][j], summation[i][x] + solution[i-1][j-x])

    print(solution)
    return solution
'''
def beuty(idx, pcur, n, k, p, *dp):
    '''Recursive function to find max solution'''
    if idx > n or pcur < p:
        return 0

    if dp[idx][pcur] != -1:
        return dp[idx][pcur]

    ans = 0
    for j in range(k):
        if pcur < j:
            break
        ans = max(ans, arr[idx][j] + beuty(idx+1, pcur-j, n, k, p, *dp))

for t in range(cases):
    n, k, p = list(map(int, input().split()))
    beauty_values = []
    for _ in range(n):
        beauty_values.append(list(map(int, input().split())))

    maximum = max_solution(beauty_values, n, k, p)

    print('Case #{}: {}'.format(t+1, maximum[n-1][p-1]))
