'''
Kayla Lange
February 13, 2026
file_content_stats.py

Description:
This program reads a text file and provides statistics about the content of the file, 
including total lines, average words per line, average characters per line, 
longest sentence by character count, and shortest sentence by character count.    
'''

import os

from pathlib import Path 

def get_file_name(): #Prompt user until valid file path is entered
    while True:
        file_path = input("\n-----Welcome to File Content Statistics Tool-----\n" \
        "\nPlease enter the full path and  name of the text file to assess (example.txt):\n")
    
        file_path = Path(file_path)

        if file_path.is_file():
            return file_path
        else:
            print("File does not exist. Please try again.")
            print('An example of the file pathway is: C:\\Users\\username\\Documents\\file.txt') 
    
def get_file_contents(file_path): #Reads the file 
    with open(file_path, 'r') as file:
        rows = file.readlines()
        clean_rows = [row.strip() for row in rows]
    return clean_rows
    
def print_rows(clean_rows): #prints each line with a line number in front of it
        for i, row in enumerate(clean_rows, 1):
            print(f'{i}: {row}')

def print_statistics(new_rows, characters_per_line): #Prints Statistics about the file content
    print(f'Total lines: {total_lines(new_rows)}')
    print(f'Average number of words per line: {average_words(new_rows):.02f}') 
    print(f'Average number of characters per line: {average_characters(new_rows, characters_per_line):.02f}')
    print(f'The longest sentence (by character count): {longest_sentence(new_rows, characters_per_line)}')
    print(f'The shortest sentence (by character count): {shortest_sentence(new_rows, characters_per_line)}') 

def stats_rows(clean_rows): #Removes the header row and any empty rows from the list of rows
    new_rows = clean_rows[1:]
    new_rows = [row for row in new_rows if row != '']
    return new_rows
    

def total_lines(new_rows): #Counts the total number of lines in the file
    total_lines = 0
    total_lines += len(new_rows)
    return total_lines

def average_words(new_rows): #Counts the number of words per line in the file
    words_per_line = []
    for row in new_rows:
        total_words = 0
        words = row.split()
        total_words += len(words)
        words_per_line.append(total_words)
    words_per_line = sum(words_per_line)
    average_words = words_per_line / total_lines(new_rows)
    return average_words
    

def characters(new_rows): #Counts the number of characters per line in the file, excluding spaces
    characters_per_line: list[int] = []
    for row in new_rows:
        total_characters = 0
        words = row.split()
        characters = [len(characters) for characters in words]
        total_characters = sum(characters)
        characters_per_line.append(total_characters)
    return characters_per_line

def average_characters(new_rows, characters_per_line): #Calculates the avg number of characters per line 
    characters_per_line = sum(characters_per_line)
    average_characters = characters_per_line/ total_lines(new_rows)
    return average_characters

def longest_sentence(new_rows, characters_per_line): #Finds the longest sentence
    longest_sentence = max(characters_per_line)
    characters_per_line.index(longest_sentence)
    return (f'{new_rows[characters_per_line.index(longest_sentence)]}')

def shortest_sentence(new_rows, characters_per_line): #Finds the shortest sentence
    shortest_sentence = min(characters_per_line)
    characters_per_line.index(shortest_sentence)
    return (f'{new_rows[characters_per_line.index(shortest_sentence)]}')

def repeat_program(): #Asks the user if they want to repeat the program
    repeat = input("\nWould you like to analyze another file? (y/n): ")
    return repeat.lower() == 'y'

def main(): #Main function that calls the other functions to execute the program
    file_path = get_file_name()
    clean_rows = get_file_contents(file_path)    


    print(f'\nReading from {file_path}:\n')
    print_rows(clean_rows)

    print('\n---Text Scores---\n')
    print('These statistics do not include blank lines or the first line of the file.\n')
    new_rows = stats_rows(clean_rows)
    characters_per_line = characters(new_rows)
    print_statistics(new_rows, characters_per_line)

if __name__ == "__main__": #Calls the main function to execute the program
    while True:
        main()
        if not repeat_program():
            print("Thank you for using the Text Content Statistics Tool. Goodbye!")
            break