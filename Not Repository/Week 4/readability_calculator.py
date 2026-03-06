'''
Kayla Lange
February 13, 2026
readability_calculator.py

Description:
This program reads a text file and provides statistics about the readability of the content of the file,
including the Flesch Reading Ease score and the Flesch-Kincaid Grade Level.     
'''

import nltk
import pyphen 

from pathlib import Path 


def get_file_name(): #Prompt user until valid file path is entered
    while True:
        file_name = input("\n-----Welcome to the Text Reading Difficulty Analysis Tool-----\n" \
        "\nPlease enter the full path and  name of the text file to assess (example.txt):\n")
    
        file_path = Path(file_path)

        if file_path.is_file():
            return file_path
        else:
            print("File does not exist. Please try again.")
            print('An example of the file pathway is: C:\\Users\\username\\Documents\\file.txt') 

def get_file_contents(filename): #Reads the contents of the file and formats it for analysis
    with open(filename, 'r') as file:
        content = file.read().replace('\n', ' ')
    return content

def get_word_count(contents) -> int: #Counts the number of words in the file   
    words = contents.split()
    word_count = len(words)

    return word_count
    
def get_sentence_count(contents) -> int: #Counts the number of sentences in the file
    sentences = nltk.sent_tokenize(contents)
    sentence_count = len(sentences)
    
    return sentence_count

def get_syllable_count(words): #Counts the number of syllables in the file
    dic = pyphen.Pyphen(lang='en_US')

    syllable_count = 0

    for word in words:
            if word.isalpha():
                hyphenated = dic.inserted(word)
                syllable_count += hyphenated.count('-') + 1
            
    return syllable_count

def get_flesch_reading_ease_score(word_count, sentence_count, syllable_count): #Calculates the Flesch Reading Ease score
    flesch_reading_ease = 206.835 - (1.015 * (word_count / sentence_count)) - (84.6 * (syllable_count / word_count))
    return flesch_reading_ease

def get_flesch_reading_grade_level(word_count, sentence_count, syllable_count): #Calculates the Flesch-Kincaid Grade Level)
    flesch_kincaid_grade_level = (0.39 * (word_count / sentence_count)) + (11.8 * (syllable_count / word_count)) - 15.59
    return flesch_kincaid_grade_level

def print_readability_score(word_count, sentence_count, syllable_count): #Prints Readability Scores
    print(f'The Flesch Reading Ease Score is: {get_flesch_reading_ease_score(word_count, sentence_count, syllable_count):.2f}')
    print(f'The Flesch-Kincaid Grade Level is: {get_flesch_reading_grade_level(word_count, sentence_count, syllable_count):.2f}') 

def repeat_program(): #Asks the user if they want to repeat the program
    repeat = input("\nWould you like to analyze another file? (y/n): ")
    return repeat.lower() == 'y'



def main(): #Main function that calls the other functions to execute the program
    file_path = get_file_name()
    contents = get_file_contents(file_path)

    print(f'\nProcessing {file_path}:\n')

    print('\n*****Text Scores*****\n')
    word_count = get_word_count(contents)
    sentence_count = get_sentence_count(contents)
    words = contents.split()
    syllable_count = get_syllable_count(words)
    
    print_readability_score(word_count, sentence_count, syllable_count)


if __name__ == "__main__": #Calls the main function to execute the program
    while True:
        main()
        if not repeat_program():
            print("Thank you for using the Text Reading Difficulty Analysis Tool. Goodbye!")
            break