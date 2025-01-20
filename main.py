import random
from termcolor import colored  # for printing colored text

# Game Instructions
def print_menu():
    print("Let's Play Wordle")
    print("Type a 5-letter word below and press enter. You have 6 tries to guess the random word.\n")

# Chooses a word from "wordbank.txt"
def read_random_word():
    with open("wordbank.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

# Valid word list for quick lookup
with open("wordbank.txt") as f:
    valid_words = set(f.read().splitlines())

# Start the main program
print_menu()

play_again = ""

while play_again != "q":
    word = read_random_word()
    attempts_left = 6
    guesses = []  # Store each formatted guess for visual stacking

    print("Enter your guesses below. You have 6 attempts to guess the word.\n")

    while attempts_left > 0:
        guess = input().lower()  # No repeated prompt for each guess

        # Validate input
        if len(guess) != 5:
            print("Your guess must be exactly 5 letters. Try again.")
            continue

        # Build formatted guess result
        result = ""
        for i in range(5):
            if guess[i] == word[i]:
                result += colored(guess[i], 'green')
            elif guess[i] in word:
                result += colored(guess[i], 'yellow')
            else:
                result += guess[i]

        # Store the formatted guess for display
        guesses.append(result)

        # Clear the previous output and show all guesses
        print("\nGuesses so far:")
        for past_guess in guesses:
            print(past_guess)

        # Check if the guess was correct
        if guess == word:
            print(colored(f"\nCongratulations! You guessed the word in {6 - attempts_left + 1} tries!", 'green'))
            break

        attempts_left -= 1

    if guess != word:
        print(f"\nSorry, the word was: {word}")

    play_again = input("Want to play again? Type 'q' to exit or press Enter to continue: ").lower()


#/n is a new line
#The splitlines() method splits a string into a list. The splitting is done at line breaks.
#
