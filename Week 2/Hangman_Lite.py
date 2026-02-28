'''
Docstring for CPSC-50000_Sping2026.Hangman_Lite
Kayla Lange
01/31/2026
Hangman_Lite.py

Description:
Word guessing before I look at the provided tips or starter code. Work in progress.
'''

import random

#game_intro
print("\nWelcome to guess the letter!\n")
print('Please guess one letter at a time.\n')
input('\nPress [ENTER] to begin the game: ')

random_word = 'alfredo'
length_word = len(random_word)
hidden_word =  ("_" * len(random_word)) #Word hidden as underscores
new_hidden_word = hidden_word
    

def update_hidden_word(user_guess, hidden_word, new_hidden_word):
    for i in range(length_word):
        if user_guess == random_word[i]:
            new_hidden_word = new_hidden_word[:i] + user_guess + new_hidden_word[i+1:]
            print(f'Your current word is: {new_hidden_word}')
        else:
            new_hidden_word = hidden_word
            print(f'Your current word is: {new_hidden_word}')
            break
    return new_hidden_word



def check_for_invalid_entry(user_guess):
    if len(user_guess) != 1:
        print('You must enter a single letter only.')
    if not user_guess.isalpha():
        print('You can only guess letters!')
    else:
        return True
    return False


correct_guess_list = []
def add_correct_guess(user_guess, correct_guess_list):
    new_letter = user_guess
    if new_letter:
        correct_guess_list.append(new_letter)
        print(f'Correct guesses: {correct_guess_list}')

incorrect_guess_list = []
def add_incorrect_guess(user_guess):
    new_letter = user_guess

    if new_letter:
        incorrect_guess_list.append(new_letter)
        print(f'Incorrect guesses: {incorrect_guess_list}')



#counters before start:
incorrect_guess = 0
correct_guess = 0
guess_counter = 0
guesses_remaining = (len(random_word) * 2)

print(f'Your current word is: {hidden_word}')
print(f'You have {guesses_remaining} guesses.')

while correct_guess < length_word and guess_counter <= guesses_remaining:
    user_guess = input('\nGuess a letter: ').lower()
    if check_for_invalid_entry(user_guess) == user_guess: 
        user_guess = user_guess
    else:
        continue
        
    if user_guess in random_word:
        if user_guess in random_word and user_guess not in correct_guess_list and user_guess not in incorrect_guess_list:
            print('\nThat guess is correct.')
            correct_guess = correct_guess + 1
            add_correct_guess(user_guess, correct_guess_list)
            new_hidden_word = update_hidden_word(user_guess, hidden_word, new_hidden_word)
        else:
            print('\nYou have already guessed that letter. Please try again.')
            continue
    else:
        print('\nThat guess is incorrect.')
        incorrect_guess = incorrect_guess + 1
        add_incorrect_guess(user_guess)
        new_hidden_word = update_hidden_word(user_guess, hidden_word, new_hidden_word)
       
    guess_counter = incorrect_guess + correct_guess
    guesses_remaining = (len(random_word) * 2) - guess_counter
    print(f'You have {guesses_remaining} guesses remaining.')
    continue

if correct_guess == length_word:
    print('\nCongratulations! You guessed the word!')
if guess_counter == length_word:
    print('\nSorry, you have no more guesses. Better luck next time!')

