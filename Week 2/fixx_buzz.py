# if a number  is easily divisible by 3 fizz, divisble by 5 buzz, divisble by both fizzbuzz for the numbers 1 through 100 inclusive
#Stopping number is exclusive so you would do 1-101
# Print number if it is not fizz or buzz or fizzbuzz

# 1 2 3 Fizz 4 Buzz Fizz etc
'''
for number in range(0, 101):
    if number % 3 == 0 & number % 5 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 5 == 0:
        print('Fizz')
    else:
        print(number)
'''
# Could use ChatGPT, is this number easily divisible by another number
# in python show me the modulo function- 10 modulo 3 returns the remainder, so we can apply this function 
# One an IF condition is true, it won't evaluate after that so move fizzbuzz to the beginning

for number in range(1, 101):
    output = ''
    if number % 3 == 0: output = 'Fizz' # We don't have to have an additional line for the result of the condition with one statement
    if number % 5 == 0: output = output + 'Buzz'
    if output == '': output = number