'''
Problem A. Common Anagrams

Problem
Ayla has two strings A and B, each of length L, and each of which is made of uppercase English alphabet letters. She would like to know how many different substrings of A appear as anagrammatic substrings of B. More formally, she wants the number of different ordered tuples (i, j), with 0 ≤ i ≤ j < L, such that the i-th through j-th characters of A (inclusive) are the same multiset of characters as at least one contiguous substring of length (j - i + 1) in B.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with one line, containing L: the length of the string. The next two lines contain one string of L characters each: these are strings A and B, in that order.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the answer Ayla wants, as described above.

Algorithm
1. Take set of substring from 0 to L in A
2. Take anagrams in B
3. for each substring in A count match anagrams in B 

Author: Wesin Alves
'''

def is_anagram(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    if alist1 == alist2:
    	matches = True
    else:
    	matches = False


    '''
    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False
	'''
    return matches

def substrings(s1,s2, L):
	subs1 = []
	subs2 = []

	for j in range(L):
		for i in range(j+1):
			subs1.append(s1[i:j+1])

	for k in range(L):
		for q in range(k+1):
			subs2.append(s2[q:k+1])

	return subs1,subs2


t = int(input())
for n in range(1, t + 1):
	num_anagrams = 0
	L = int(input())
	A = input()
	B = input()
	#print(L,A,B)

	subsA, subsB = substrings(A,B,L)
	#print(subsA)
	#print(subsB)
	count = 0
	for ii in range (len(subsA)):
		for jj in range(len(subsB)):
			if is_anagram(subsA[ii],subsB[jj]) == True:
				count += 1
				break
		

	print("Case #{}: {}".format(n, count))