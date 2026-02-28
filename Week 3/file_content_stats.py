import os

from pathlib import Path 

def user_file_name(): #Collects the file name from the user
    file_name = input("\n-----File Content Statistic Reader-----\n" \
    "\nEnter the location of your text file:\n")
    return file_name

def check_file_name(filename): #Checks if the file exists at the given location
    file_path = Path(filename)
    if file_path.exists():
        return True
    else:
        print("File does not exist. Please try again.")
        print('An example of the file pathway is: C:\\Users\\username\\Documents\\file.txt)')
        return False
    
def format_rows(filename): #Reads the file and prints each line with a line number in front of it
    with open(filename, 'r') as file:
        rows = file.readlines()
        clean_rows = [row.strip() for row in rows]
    return clean_rows
    
def print_rows(clean_rows): #Reads the file and prints each line with a line number in front of it
        for i, row in enumerate(clean_rows, 1):
            print(f'{i}: {row}')

def analyze_rows(clean_rows, filename): #Removes the header row and any empty rows from the list of rows
    clean_rows = format_rows(filename)
    header = clean_rows[0]
    for rows in clean_rows:
        if rows == header or rows == '':
            clean_rows.remove(rows)
        else:
            return rows


def total_lines(analyze_rows, clean_rows): #Counts the total number of lines in the file
    rows = analyze_rows(clean_rows)
    total_lines = 0
    for rows in analyze_rows(clean_rows):
        total_lines += len(rows)
    return total_lines

def words_per_line(analyze_rows): #Counts the number of words per line in the file
    total_words = 0
    for rows in analyze_rows:
        words = rows.split()
        total_words += len(words)
    return total_words

def average_words_per_line(total_words, analyze_rows): #Calculates the average number of words per line in the file by dividing the total number of words by the total number of lines
    average_words = total_words / total_lines(analyze_rows)
    return average_words

def characters_per_line(analyze_rows, clean_rows, filename): #Counts the number of characters per line in the file, excluding spaces
    rows = [analyze_rows(clean_rows, filename)]
    total_charcters = 0
    for rows in rows:
        words = rows.split(' ')
        characters = [len(characters) for characters in words]
        total_characters = sum(characters)
    return total_characters

def average_characters_per_line(analyze_rows, clean_rows, filename): #Calculates the average number of characters per line in the file by dividing the total number of characters by the total number of lines
    average_characters = characters_per_line(analyze_rows, clean_rows, filename) / total_lines(analyze_rows, clean_rows)
    return average_characters

def sentence_length(analyze_rows, filename, clean_rows): #Finds the longest sentence in the file by character count and word count
    rows = analyze_rows
    sentence_length_by_characters = 0
    for rows in analyze_rows:
        total_characters = characters_per_line(analyze_rows, clean_rows, filename)
        sentence_length_by_characters = total_characters
        return sentence_length_by_characters

def longest_sentence_by_character_count(analyze_rows, sentence_length_by_characters): #Finds the longest sentence in the file by character count
    longest_sentence = sentence_length(analyze_rows).max(sentence_length_by_characters)
    return longest_sentence
        
def shortest_sentence_by_character_count(analyze_rows, sentence_length_by_characters): #Finds the longest sentence in the file by character count
    shortest_sentence = sentence_length(analyze_rows).min(sentence_length_by_characters)
    return shortest_sentence
        

def print_statistics(clean_rows, total_words, total_characters, sentence_length_by_characters): #Prints the statistics of the file
    print(f'Total lines: {total_lines(analyze_rows, clean_rows)}')
    print(f'Average number of words per line: {average_words_per_line(total_words, analyze_rows)}')
    print(f'Average number of characters per line: {average_characters_per_line(total_characters, analyze_rows)}')
    print(f'The longest sentence (by character count): {longest_sentence_by_character_count(analyze_rows, sentence_length_by_characters)}')
    print(f'The shortest sentence (by character count): {shortest_sentence_by_character_count(analyze_rows, sentence_length_by_characters)}')
    
def main(): #Main function that calls the other functions to execute the program
    filename = user_file_name()
    does_file_exist = check_file_name(filename)

    if not does_file_exist:
        print("Exiting program.")
        return

    print(f'\nReading from {filename}:\n')
    clean_rows = format_rows(filename)
    print_rows(clean_rows)

    print('\n---Sentence Statistics---\n')
    analyze_rows = [analyze_rows(clean_rows, filename)]
    total_words = words_per_line(analyze_rows(clean_rows, filename))
    total_characters = characters_per_line(analyze_rows, clean_rows, filename)
    sentence_length_by_characters = sentence_length(clean_rows, filename, analyze_rows(clean_rows, filename))
    print_statistics(clean_rows, total_words, total_characters, sentence_length_by_characters)

main()