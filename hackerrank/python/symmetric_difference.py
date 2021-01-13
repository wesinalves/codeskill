'''
###############
Task
###############

Given 2 sets of integers, M and B, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N
but do not exist in both.

###############
Input Format
###############

The first line of input contains an integer, M.
The second line contains space-separated integers.
The third line contains an integer, N.
The fourth line contains space-separated integers.

###############
Output Format
###############

Output the symmetric difference integers in ascending order, one per line.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
m_set = set(map(int,input().split(' ')))
N = int(input())
n_set = set(map(int,input().split(' ')))

symmetric_difference = m_set.difference(n_set)
symmetric_difference.update(n_set.difference(m_set))
ordered_list = list(symmetric_difference)
ordered_list.sort()
print(' \n'.join(map(str, ordered_list)))