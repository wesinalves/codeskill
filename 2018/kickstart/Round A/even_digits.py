'''
Code for google kickstart
Round A - Even Digits
Wesin Ribeiro
2020

##############
Problem
##############
This calculator only has a display, a plus button, and a minus button.
The integer N is displayed on the calculator display.
Pressing the plus button increases the current number displayed on the calculator
display by 1. Similarly, pressing the minus button decreases the current number
displayed on the calculator display by 1.
The calculator does not display any leading zeros.
Determine the minimum number of button presses to make the calculator
display an integer with no odd digits.

##############
Comments
##############
a number is even if the module operation by 2 is 0.

'''

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        button_inscrease = 0
        button_decrease = 0

        n = int(input())

        print('Case #{}: {}'.format(t+1, ans))

main()