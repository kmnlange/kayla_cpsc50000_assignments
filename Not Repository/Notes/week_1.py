#Program: First week Examples
#Date: 25 January 2026


print('***** First Week Examples *****') # print a string literal (single or double quote marks
print("This is Kayla's first week program") # Double quote used to go around single quote

print('Kayla', 'Is', 'Close to', 25, 'years', 'old')
print('Kayla' + ' Is' + ' Close to ' + str(25) + ' years' + ' old') #Concantenation

name= 'Kayla'
age=25
#Formatted Print Statement
print(f'{name} Is Close to {age} years old') #String interplation- embedding data into string directly

'''
name= 'Kayla'
age= 24
''' #Multiline comment, not code, can be double quotes as well

name = input('Please enter your first name:')
age = input('Please enter your age') # User input comes to you as a string

age = int(age) + 1 # Conversion to get user data to get a numeric instead of a string

age = int(input('Now enter your age')) # Another option

age = 10. # Float data type with decimal

age = age / 2 + 1 #PEMDAS

# Formatted Print Statement
print(f'The new age is {age}')
 
if age < 20:
    print(f'At your age of {age}, you are young')
    print('This is a second line attached to the trufulness of the previous line') #Indentation to define scope
    if age < 10:
        print('At {age} years of age, you are very young.')
if age >= 20 and <= 40
    print(f'At {age} years of age-- you are living your best life.') #you can do this but there is a better way

if age < 20: #Short-circuiting statements
    print(f'At your age of {age}, you are young')
    print('This is a second line attached to the trufulness of the previous line') #Indentation to define scope
    if age < 10:
        print('At {age} years of age, you are very young.')
elif age <= 40:
    print(f'At {age} years of age--you are living your best life.')
elif age <= 60
    print(f'At your age of {age} you are getting up there.')
else:
    print('Okay, you should be wiser now.')

print('This is the end of my program.')




# Formatted Print Statement
print(f'{name} Is Close to {age} years old')

# Example of Multi-Line String
text = '''This is an example of
                multi-line text in a 
                    Python program'''

