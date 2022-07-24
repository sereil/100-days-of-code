#Hangman Game

#Day 7 of 100 Days of Code

#Sereil-Vann Phlek - 2022-07-23

#Step 5
import random
import hangman_words
import hangman_art
import os
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo
game_over_art = hangman_art.logo
print(f"""{logo}
Welcome to the Hangman game!
""")
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

wrong_guesses = []

while not end_of_game:    

    guess = input("Guess a letter: ").lower()
    os.system('CLS')
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}!")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            #This print is out of order and I kind of don't like it anyways since the list shows if they got it right or not.
            # print(f"{guess} is correct!")
            

    #Check if user is wrong.
    print(f"Previous guesses: {wrong_guesses}")  
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.               
        print(f"{guess} is incorrect! You lose a life.")
        wrong_guesses.append(guess)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"""You lose.
            {game_over_art}""")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stages = hangman_art.stages
    print(stages[lives])