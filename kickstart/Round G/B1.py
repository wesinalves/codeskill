'''
Problem B. Combining Classes

Problem
Can you help Supervin answer all of his questions? Since there may be many answers, instead of outputting all of them, 
output proof that you have answered them: the sum of (Si × i) for all 1 ≤ i ≤ Q, where Si is the answer to the i-th question.

Algorithm
1. generate arrays X,Y,Z
2. compute arrays L, R, K
3. select S
4. compute scores

Author: Wesin Alves
'''
import numpy as np

def gen_array(x1,x2,a1,b1,c1,m1,n):
	X = []
	X.append(x1)
	X.append(x2)
	for i in range(2,n):
		X.append( (a1*X[i-1] + b1*X[i-2] + c1) % m1 )

	return X


t = int(input())
for l in range(1, t + 1):
	n, q = input().split(" ")
	# generate arrays
	x1,x2,a1,b1,c1,m1 = input().split(" ")
	X = []
	X = gen_array(int(x1),int(x2),int(a1),int(b1),int(c1),int(m1),int(n))
	
	y1,y2,a2,b2,c2,m2 = input().split(" ")
	Y = []
	Y = gen_array(int(y1),int(y2),int(a2),int(b2),int(c2),int(m2),int(n))
	
	z1,z2,a3,b3,c3,m3 = input().split(" ")
	Z = []
	Z = gen_array(int(z1),int(z2),int(a3),int(b3),int(c3),int(m3),int(q))



	L = np.minimum(X[:int(n)], Y[:int(n)]) + 1
	R = np.maximum(X[:int(n)],Y[:int(n)]) + 1
	K = np.array(Z[:int(q)]) + 1

	scores = []

	for i in range(len(L)):
		notes = np.arange(L[i],R[i]+1, dtype='int8')
		for note in notes:
			scores.append(note)

	scores.sort(reverse=True)


	S = []
	for j in range(len(K)):
		if K[j] - 1 < len(scores):
			S.append(scores[K[j] - 1])
		else:
			S.append(0)
	
	sum_of_sxi = 0
	for k,s in enumerate(S):
		sum_of_sxi += s * (k + 1)

	
	print("Case #{}: {}".format(n, sum_of_sxi))
