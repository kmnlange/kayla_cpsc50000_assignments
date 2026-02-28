# The Collatz Conjecture
'''
If you begin with any non-zero, positive, integer greater than 1:
-- if the number is even, divide by 2
-- if the number is odd, multiply by 3 and add one
-- print the number and loop again

You will eventually return to one
'''

# Supose we begin with 15:

'''
10
5
16
8
4
2
1
'''

# Get the starting number from the user. Then iterate as many times as necessary,
# following the rules above, until we get to 1-- and then stop.

User_Input = input('Please enter a postitive integer greater than 1: ')
User_Input = int(User_Input)
print(f'You have entered: {User_Input}.')

Iteration = 0
Numbers = list()
Numbers.append(User_Input)

while User_Input > 1:
    if User_Input % 2 == 0:
        Iteration = Iteration + 1
        User_Input = User_Input/2
        Numbers.append(User_Input)
    else:
        Iteration = Iteration + 1
        User_Input = (User_Input * 3) + 1
        Numbers.append(User_Input)
    
print(Numbers)
print(f' A total of: {Iteration} iterations.')