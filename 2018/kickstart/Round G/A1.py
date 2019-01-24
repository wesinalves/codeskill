'''
Problem A. Product Triplets

Problem
Given N integers A1, A2, ..., AN, count the number of triplets (x, y, z) (with 1 ≤ x < y < z ≤ N) such that at least one of the following is true:

Ax = Ay × Az, and/or
Ay = Ax × Az, and/or
Az = Ax × Ay

Algorithm
1. Take triplets
2. check conditions
3. if conditions true, increment count 

Author: Wesin Alves
'''

import numpy as np	

t = int(input())

for l in range(1, t+1):
	count = 0;
	n = int(input())
	A = input().split(' ')
	A[:] = [int(s) for s in A]

	A_sorted = np.float64(np.sort(A))
	
	# check conditions
	for z in range(len(A_sorted),0,-1):
		for y in range(z-1,0,-1):
			for x in range(y-1,0,-1):
					
				if(A_sorted[x-1] == A_sorted[y-1] * A_sorted[z-1]):
					count += 1
				elif(A_sorted[y-1] == A_sorted[x-1] * A_sorted[z-1]):
					count += 1
				elif(A_sorted[z-1] == A_sorted[x-1] * A_sorted[y-1]):
					count += 1

	print("Case #{}: {}".format(l, count))

