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

>>>
Kickstart web inteface says this script has a runtime error, but I can't figure out where error is.
Maybe the algorithm is not efficient even for the small dataset. I'll jump to the next challenge,
after that I'll try again.

'''
def check_first_odd(digits):
    '''check for first digit is odd'''
    first = -1
    for d in range(len(digits)):
        if (int(digits[d]) % 2) != 0:
            first = d
            return first
    return first

def leftmost_beutiful(number):
    '''Find largest beautiful from N
        X -> largest beautiful number < N
        - deacreasing first odd digits
        - replacing all digits to the right by 8
        - drop the leadings 0
    '''
    x_number = list(number)
    first_index = check_first_odd(number)
    if first_index != -1:
        first_str = number[first_index]
        new_first = int(first_str) - 1
        x_number[first_index] = str(new_first)
        if len(x_number) > 1:
            x_number[first_index+1:] = ['8' for _ in range(len(x_number[first_index+1:]))]
            if new_first == 0:
                x_number.pop(first_index)
    return ''.join(x_number)

def rightmost_beautiful(number):
    '''Find smallest beautiful from N
        Y - smallest beautiful number > N
        - increasing firs odd digits
        - replaciong all digits to the right by 0
        - if first is 9, replace left digit by next even
        - if left digit to the first odd is 8, replace left digit by next even until non-8
        - if left digit continues 8 or first is 9, add 2 on he left
    '''
    y_number = list(number)
    first_index = check_first_odd(number)
    if first_index != -1:
        first_str = number[first_index]
        y_number[first_index+1:] = ['0' for _ in range(len(y_number[first_index+1:]))]
        if first_str == '9' and first_index > 0:
            y_number[first_index] = '0'            
            index = first_index - 1
            while y_number[index] == '8':
                y_number[index] = '0'
                index -= 1
            left = int(y_number[index]) + 2
            y_number[index] = str(left)
        elif y_number[0] == '9':
            y_number[0] = 2
            y_number[1:] = ['0' for _ in range(len(y_number[1:]))]
            y_number.append(0)
        else:
            new_first = int(first_str) + 1
            y_number[first_index] = str(new_first)            
    
    return ''.join(y_number)
    



def main():
    '''Main Function'''
    tests = int(input())
    for t in range(tests):
        n = input()
        X = leftmost_beutiful(n)
        Y = rightmost_beautiful(n)
        M = int(n) - int(X)
        P = int(Y) - int(n)
        lower = min(M,P)
        if lower == M:
            ans = M
        if lower == P:
            ans = P
        print('Case #{}: {}'.format(t+1, ans))

main()