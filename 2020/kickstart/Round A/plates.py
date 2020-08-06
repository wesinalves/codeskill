'''
n -> stacks
k -> plates
p -> chosen plate
'''

cases = int(input())
# def possible_solution(matrix_values, num_stacks, num_plates, plates):
#     '''Take all possible solution for P plates'''
#     solutions = []

#     for i in range(num_stacks):
#         for j in range(num_plates):


#     return solutions

for t in range(cases):
    n, k, p = list(map(int, input().split()))
    beauty_values = []
    for i in range(n):
        beauty_values.append(list(map(int, input().split())))

    #maximum_total_sum = max(possible_solution(beauty_values, n, k, p))
    print(len(beauty_values), len(beauty_values[0]))


    #print('Case #{}: {}'.format(t+1, maximum_total_sum))
