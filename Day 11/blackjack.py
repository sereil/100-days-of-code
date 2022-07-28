############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## If the dealer's hand is 17 or more, the dealer will stand.

import art
import random
import os

logo = art.logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    random_card = random.choice(cards)
    return random_card

def calculate_score(hand):
    score = sum(hand)
    if score == 21:
        hand_state = "Blackjack"
    elif score > 21:
        hand_state = "Bust"
    else:
        hand_state = "Playable"
    hand_dict = {score:hand_state}
    return hand_dict

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play_game == "y":
    player_hand = []
    dealer_hand = []    
    
    for card in range(0,2):        
        player_hand.append(draw_card())

    dealer_hand.append(draw_card())

    keep_playing = True
    # bust = False
    # winner = False
    # player_move == "hit" or bust == False
    while keep_playing == True:

        dealer_score = sum(dealer_hand)
        player_score = sum(player_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's cards: {dealer_hand}, current score: {dealer_score}") 
        player_move = input("What is your next move? Type 'hit' or 'stand': ")
#TODO-1: Find a way to merge a "Hit" and a "Stand" in one function
        if player_move == "hit":
            #TODO-3: Implement Ace valued at 11 or 1
            player_hand.append(draw_card())
            player_score = sum(player_hand)
            result = calculate_score(player_score)
            game_state = result[player_score]
            if game_state != "Playable":
                keep_playing = False
                print(f"You {game_state}ed!")

        elif player_move == "stand":
            while dealer_score < 16:                
                dealer_hand.append(draw_card())
                dealer_score = sum(dealer_hand)
                result = calculate_score(dealer_score)
                game_state = result[dealer_score]
                if game_state != "Playable":
                    keep_playing = False
                    print(f"The dealer {game_state}ed!")
            keep_playing = False

#TODO-2: Print Winner
print(f"Your cards: {player_hand}, current score: {player_score}")
print(f"Dealer's cards: {dealer_hand}, current score: {dealer_score}") 


