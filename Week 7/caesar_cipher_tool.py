'''
Kayla Lange

March 03, 2026

Description:
This program implements a Caesar Cipher tool that allows users to
encrypt and decrypt text files. The program reads an input file,
applies the Caesar cipher algorithm, and writes the results to a
new output file in the same directory.
'''

from pathlib import Path
from caesar_cipher import CaesarCipher

def display_menu(): # Displays the main menu options for the user.
    print('\n-----Menu Options-----\n')
    print('E -- Encrypt a plain text file')
    print('D -- Decrypt a mystery encrypted file (no key known)')
    print('x -- Exit the Program')


def get_input_file(): # Prompts the user for a valid file path and returns the file if it exists.
    while True:
        file = input("\nPlease enter the full path and  name of the text file to begin (example.txt):\n")

        input_file = Path(file)

        if input_file.is_file(): return input_file
        else:
            print("\nFile does not exist. Please try again." \
                    "\nAn example of the file pathway is: C:\\Users\\username\\Documents\\file.txt\n")
        
def read_input_file(input_file) -> list: # Opens the log file and returns the list of log entries as lines.
    text = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            text.append(line.strip())   

    return text
    
def write_encryption_file(input_file, encrypted_lines): # Writes encrypted lines to a new output file in the same directory.
    output_path = input_file.parent / (input_file.stem + '_encrypted.txt')

    with open (output_path, 'w') as file:
        for line in encrypted_lines:
            file.write(line + '\n')

    return output_path
    
def encrypt(): # Encrypts each message from the input file using the provided key.
    input_file = get_input_file()
    text = read_input_file(input_file)

    print(f'Encrypting {len(text)} lines...\n')

    encrypted_lines = []

    for line in text: 
        key, message = line.split('|')
        key = int(key)
        cipher = CaesarCipher(key)
        encrypted_message = cipher._encrypt(message)
        encrypted_lines.append(encrypted_message)

    print("\nHere is the path to your new file: \n", write_encryption_file(input_file, encrypted_lines))

    cont()

def get_frequency_count(line): # Counts the frequency of alphabetic characters in a line of text.
        encrypted_message = " ".join(line).lower()

        frequency_count = {}

        for char in encrypted_message:
            if char.isalpha():
                frequency_count[char] = frequency_count.get(char, 0) + 1

        return frequency_count

def get_possible_key(frequency_count, i): # Generates a possible Caesar cipher key using frequency analysis.
    sorted_letters = sorted(frequency_count, key = frequency_count.get, reverse = True)

    most_common_letters = ['e','t','a','o','i','n','s','h','r','d','l','u', 
                           'c','m','f','y','w','g','p','b','v','k','x','q','j','z']
    
    encrypted_letter = sorted_letters[i % len(sorted_letters)]

    hypothesis  = most_common_letters[i]

    possible_key = (ord(encrypted_letter) - ord(hypothesis)) % 26
    
    return possible_key        

def is_decryption_correct(preview):    # Displays a decrypted preview and asks the user if it is correct.

    user_input = input(f'Does this look correct? \n{preview}\n (y/n): ').strip().lower()
    
    return user_input == 'y'

def write_decryption_file(input_file, decrypted_lines): # Writes the confirmed decrypted lines to a new output file.
    output_path = input_file.parent / (input_file.stem + '_decrypted.txt')

    with open (output_path, 'w') as file:
            for line in decrypted_lines:
                file.write(line + '\n')

    return output_path

def decrypt(): # Attempts to decrypt each line by testing possible keys until the user confirms the correct result.
    input_file = get_input_file()
    text = read_input_file(input_file)

    decrypted_lines = []
    
    for line in text:
        print (f'\nDecrypting line: \n{line}\n')
        frequency_count = get_frequency_count(line)

        i = 0

        while i < 26:
            key = get_possible_key(frequency_count, i )
            print (f'\nTesting Key {key}')

            cipher = CaesarCipher(key)
            decrypted_message = cipher._decrypt(line)
                
            if is_decryption_correct(decrypted_message): 
                decrypted_lines.append(decrypted_message) 
                break 
            else: i += 1
        
    if i == 26: print('Unable to determine correct decryption.')
    else: 
        print("\nHere is the path to your new file: \n", write_decryption_file(input_file, decrypted_lines))
        cont()

def cont():
    input('Press Enter to Continue: ')

def main(): # Main program loop 
    print('-----Welcome to the Caesar Cipher Tool.-----')

    while True:
        display_menu()
        menu_option = input('\nSelect an Option>> ').strip().casefold()

        if menu_option == 'e': encrypt()
        if menu_option == 'd': decrypt()
        if menu_option == 'x': break

if __name__=='__main__':
    main()

    print("\nThank you for using the Caesar Cipher Tool. Goodbye!")
