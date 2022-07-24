#Step 3

import random
import hangman_art
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
game_over = False

lives = 6

while game_over == False:
    guess = input("Guess a letter: ").lower()


    if chosen_word.count(guess) == 0:
        lives -=1
        print(f"Wrong! You have {lives} left")
    

    if lives <= 0:
        print("""You ran out of lives! {game_over_art}     
        """)
        game_over = True
    
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    print(display)

    if display.count("_") == 0:
        print(f"You've won!")        
        game_over = True