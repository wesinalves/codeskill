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
How to check if all numbers are even?
M -> mininum number of minus button
P -> minium number of plus button
ans = min(M,P)
------------------------------------------------------
X -> largest beautiful number < N
- deacreasing first odd digits
- replacing all digits to the right by 8
- drop the leadings 0
Y - smallest beautiful number > N
- increasing firs odd digits
- replaciong all digits to the right by 0
- if first is 9, replace left digit by next even
- if left digit to the first odd is 8, replace left digit by next even until non-8
- if left digit continues 8 or first is 9, add 2 on he left
------------------------------------------------------------
Once we know X and Y, compute M and P.

'''
def check_evens(digits):
    '''check if all digits are even'''
    even = True
    for d in str(digits):
        if (int(d) % 2) != 0:
            even = False
            return even
    return even

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        button_increase = 0
        button_decrease = 0
        n = int(input())
        all_even = check_evens(n)
        while not all_even:
            button_increase += 1
            all_even = check_evens(n + button_increase)
            if all_even:
                ans = button_increase
                break
            button_decrease += 1
            all_even = check_evens(n - button_decrease)
        
        if all_even and ans == 0:
            ans = button_decrease
            
        
        print('Case #{}: {}'.format(t+1, ans))

main()
