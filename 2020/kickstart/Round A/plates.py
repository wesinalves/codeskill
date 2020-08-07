'''
n -> stacks
k -> plates
p -> chosen plate
'''

cases = int(input())

def max_solution(matrix_values, num_stacks, num_plates, plates):
    '''Take all possible solution for P plates'''
    solution = [[0 for _ in range(plates)] for _ in range(num_stacks)]
    for i in range(1, num_stacks):
        for j in range(plates):
            solution[i][j] = 0
            for x in range(min(j, num_plates)):
                summation = sum(matrix_values[i][:x])
                solution[i][j] = max(solution[i][j], summation + solution[i-1][j-x])

    return solution

for t in range(cases):
    n, k, p = list(map(int, input().split()))
    beauty_values = []
    for _ in range(n):
        beauty_values.append(list(map(int, input().split())))

    maximum = max_solution(beauty_values, n, k, p)

    print(len(maximum), len(maximum[0]))
    print('Case #{}: {}'.format(t+1, maximum[n-1][p]))
