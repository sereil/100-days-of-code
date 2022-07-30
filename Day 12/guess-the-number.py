#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import art
import random
logo = art.logo


EASY_LEVEL = 10
HARD_LEVEL = 5

def verify_guess(guess,answer,attempts):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        attempts = -1     
    elif guess > answer:
        print("Too high.")
        attempts -=1
    elif guess < answer:
        print("Too low.")
        attempts -=1
    return attempts
    
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return HARD_LEVEL
    elif difficulty == "easy":
        return EASY_LEVEL

def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    correct_answer = random.randint(0,101)

    #Testing purposes
    print(f"Pssst, the correct answer is {correct_answer}")

    guesses_left =  set_difficulty()

    current_guess = -1
    while current_guess != correct_answer and guesses_left > 0:
        current_guess = int(input("Make a guess: "))
        guesses_left = verify_guess(guess=current_guess,answer=correct_answer,attempts=guesses_left)

        if guesses_left > 0:        
            print(f"You have {guesses_left} attempts remaining to guess the number.")
            print("Guess again.")
        elif guesses_left == 0:
            print("You've run out of guesses, you lose.")

game()

