# Primitives (intrinsics)
age = 30 # integer #python is dynamically typed and infer the integer regardless
temp = float(98.6)  # float

should_i_continue = True  #booolean

# Strings (class) -- Part of Object-Oriented Programming
# A string is an array of individual characters-- a collection of characters
# A class provides the blueprint for what will become an object.
# We refer to the object when it is in memory
name = "Kayla"
name = 'Kayla'

print(len(name))
print(name[1])

starting_string = '_' * 50  # Fills length of string (50) 
print(starting_string)
print(starting_string[49]) #change 49 to 50 and it will be out of range because the string starts at 0
print(name[-1]) # Give me the last letter
print(name[-5])# Give me the first letter "kayla"
# Phrases or whatever can be repeated a bunch with the *50 thing

opening_stanza = 'Let us go then you and I, when the evening is spread against the sky' # T.S. Elliot Poem The Love song of JL
print(opening_stanza)

words = opening_stanza.capitalize()
print(words)

words = opening_stanza.upper()
print(words)

words = opening_stanza.find('foo')

char_position = opening_stanza.find('when')
print(char_position)  #right click to rename symbol 

#Lists- a collection of things
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0])

names = list()
names.append('Kayla')
names.append('David')

mixed_list = ['David', 35, 11_592_392, True]
# Index:        0       1   2       3

name = mixed_list[1]
print(name)

name = mixed_list[0][0]

# Loops
# Python-Don't include language elements that duplicate  thee function of other elements
# Two loops in python instead of 4 (while) and (for)
# When do you use them?
# Use the 'for' loop when 
# a. you know how many times you want to loop
# b. you want to iterate through a collection of things, which includes strings

# Example A
for foo in range(5):
    print(foo)

for _ in range(5)
    print('Hello, World')

for _ in range(1, 5): #1 is the start and 5 is the end value
    print(foo)

for _ in range(1, 100): #Have to put 101 to get 100
    print(foo)

for _ in range(1, 100, 5)

for foo in range(101, 0,  -5)
    print(foo)

# Example B
for object in mixed_list:
    print(object)

for letter in opening_stanza:
    print(letter) # iterate through a collection
                    # A string is a collection of characters so you can iterate through it

# User the 'while' lopp when you want to loop 'while' condition is True

counter = 0
user_response =  'y' or user_response = 'yes'
while user_response == 'y':
    counter <= 1 # counter = counter + 1
    print(counter)
    user_response = input('Do you want to count again? y/n').lower() #input is lower case
    #it wont prevent you from typing in capital, but the return will convert what the user entered to lowercase
    #anything other than a lowercase y will end it because its not in the conditional format

while user_response.startswith('y'): 




