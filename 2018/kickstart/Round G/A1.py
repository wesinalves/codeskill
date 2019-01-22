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
import itertools as it

def take_triplets(n,X):
	triplets = list(it.combinations(X,3))
	return triplets
	

		

t = int(input())

for l in range(1, t + 1):
	count = 0;
	n = int(input())
	X = input().split(' ')
	triplets = take_triplets(n,X)

	# check conditions
	for triplet in triplets:
		if(int(triplet[0]) == int(triplet[1]) * int(triplet[2])):
			count += 1
		elif(int(triplet[1]) == int(triplet[0]) * int(triplet[2])):
			count += 1
		elif(int(triplet[2]) == int(triplet[0]) * int(triplet[1])):
			count += 1


	print("Case #{}: {}".format(l, count))