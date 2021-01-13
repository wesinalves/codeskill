'''
Code for HackerRank
Python Language Proficiency
Wesin Ribeiro

###################################
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
If a new entry overwrites an existing entry, the original insertion position is left unchanged.
'''
from collections import OrderedDict

def main():
    '''Main Function'''
    N = int(input())
    ordered_items = OrderedDict()

    for _ in range(N):
        line = input().split(' ')
        item_name = ' '.join(line[0:-1])
        price = int(line[-1])
        if not ordered_items.get(item_name):
            ordered_items[item_name] = price
        else:
            ordered_items[item_name] += price
    for key, value in ordered_items.items():
        print(key, value)

main()