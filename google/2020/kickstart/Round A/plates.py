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


def max_solution(matrix_values, num_stacks, num_plates, plates):
    '''Take all possible solution for P plates'''
    solution = [[0 for _ in range(plates)] for _ in range(num_stacks)]
    summation = precompute_sum(matrix_values, num_stacks, num_plates)
    solution[0][1:] = summation[0]
    for i in range(1, num_stacks):
        for j in range(plates):
            solution[i][j] = 0
            for x in range(min(j, num_plates)):
                solution[i][j] = max(solution[i][j], summation[i][x] + solution[i-1][j-x])

    print(solution)
    return solution