import random

# a game called "High Low"

# rules:
#  - the computer generates a random number
#  - the program then asks the user to enter a guess
#  - if the number is higher than the computer's,
#  - the output will display "Go lower."
#  - if the number is lower than the computer's,
#  - the output will display "Go higher."
#  - the user has 10 guesses to guess correctly
#  - in order to win the game

MAX_GUESSES = 10

def make_decision(guess, r):
    # 'var' is a local variable
    var = 123
    if guess > r:
        print("Go lower.")
    elif guess < r:
        print("Go higher.")


def run_game():
    # 'r' is a local variable
    r = random.random()
    r = r * 999
    r = r + 1
    r = int(r)

    # guess is also a local variable
    guess = 0
    guess_count = 0
    while guess != r and guess_count < MAX_GUESSES:
        guess = int(input("Enter a guess (1-1000): "))
        guess_count += 1
        make_decision(guess, r)

    if guess_count < MAX_GUESSES:
        print("You guessed it!")
    else:
        print(f"Sorry. The number was {r}.")


run_game()
