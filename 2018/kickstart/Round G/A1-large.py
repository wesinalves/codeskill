'''
Problem A. Product Triplets

Problem
Given N integers A1, A2, ..., AN, count the number of triplets (x, y, z) (with 1 ≤ x < y < z ≤ N) such that at least one of the following is true:

Ax = Ay × Az, and/or
Ay = Ax × Az, and/or
Az = Ax × Ay

Algorithm
>> O(n)^3
1. Take triplets
2. check conditions
3. if conditions true, increment count 

>> O(n)^2
Sort(A)

Author: Wesin Alves
'''

import numpy as np
import math	

t = int(input())

def C_nxs(n,s):
	count = 0
	if n == 0 or s > n: 
		return 0
	count = math.factorial(n) // (math.factorial(s) * math.factorial(n-s))
	return count 

for l in range(1, t+1):
	count = 0;
	n = int(input())
	A = input().split(' ')
	A[:] = [int(s) for s in A]

	A_sorted = np.float64(np.sort(A))
	occurrences = {}
	ans = 0
	Z = 0
	C_Zx3 = 0
	C_Zx2 = 0
	
	# check conditions
	for y in range(n,0,-1):
		for x in range(y-1,0,-1):
			ans = ans + occurrences.get(A_sorted[x-1] * A_sorted[y-1], 0) # it is the same to code if z = x * y
		occurrences[A_sorted[y-1]] = occurrences.get(A_sorted[y-1], 0) + 1

	Z = occurrences.get(0,0)
	C_Zx3 = C_nxs(Z,3)
	#3print(C_Zx3)
	C_Zx2 = C_nxs(Z,2)
	#print(C_Zx2)
	ans = ans + C_Zx3 + (C_Zx2 * (n - Z))
	print("Case #{}: {}".format(l, ans))

