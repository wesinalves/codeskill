'''
Problem C. Common Anagrams

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
t = int(input())
for n in range(1, t + 1):
	print("Case #{}: {}".format(n, count))