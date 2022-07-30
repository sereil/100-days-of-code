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

#It would be nice to use a class here instead of a weird JSON format dict. 
#Only doing this because I haven't learned classes yet in the course.

def initialize():
    game_state = {
        "Player":{
        "score":0,
        "hand":[],
        "status":"Playable"
        },
        "Dealer":{
        "score":0,
        "hand":[],
        "status":"Playable"
        }
    }
    return game_state


def deal_card(player_type, hand):
    random_card = random.choice(cards)
    hand.append(random_card)
    score = sum(hand)

    if score == 21:
        if len(hand) == 2:
            hand_state = "Natural Blackjack"
        else:
            hand_state = "Blackjack"
    elif score > 21:
        hand_state = "Bust"
    else:
        hand_state = "Playable"
    
    game_state[player_type]["score"] = score
    game_state[player_type]["hand"] = hand
    game_state[player_type]["status"] = hand_state
    


    
def show_state(player_type, hand):
    score = game_state[player_type]["score"]
    hand = game_state[player_type]["hand"]
    score = sum(hand)
    print(f"{player_type}'s hand: {hand}, current score: {score}")

    
    

def calculate_score(player_type, is_playable):
    if player_type == "Dealer":
        if game_state[player_type]["score"] >=17:
            is_playable = False
    if game_state[player_type]["score"] >=21:
                if 11 in game_state[player_type]["hand"]:
                    ace_position = game_state[player_type]["hand"].index(11)
                    game_state[player_type]["hand"][ace_position] = 1
                else:                    
                    is_playable = False
                    
    return is_playable

play_again = 'y'    
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_again == 'y':
    game_state = initialize()

    

    if play_game == "y":
        player_hand = []
        dealer_hand = []    
        
        for card in range(0,2):        
            deal_card(player_type="Player", hand=player_hand)
            deal_card(player_type="Dealer", hand=dealer_hand)
        

        keep_playing = True
        # bust = False
        # winner = False
        # player_move == "hit" or bust == False
        while keep_playing == True:
            os.system("CLS")
            show_state(player_type="Player", hand=player_hand)
            show_state(player_type="Dealer", hand=dealer_hand)
            player_move = input("What is your next move? Type 'hit' or 'stand': ")

            if player_move == "hit":
                deal_card(player_type="Player", hand=player_hand)  
                keep_playing = calculate_score(player_type="Player", is_playable = keep_playing)

            elif player_move == "stand":
                while game_state['Dealer']['score'] < 16:                
                    deal_card(player_type="Dealer", hand=dealer_hand)
                    keep_playing = calculate_score(player_type="Dealer", is_playable = keep_playing)
                keep_playing = False #Done

    print(f"Your cards: {player_hand}, score: {game_state['Player']['score']}")
    print(f"Dealer's cards: {dealer_hand}, score: {game_state['Dealer']['score']}") 


    player_score = game_state['Player']['score']
    dealer_score = game_state['Dealer']['score']
    if player_score > 21:
        print(f"You bust!")
    elif dealer_score > 21:
        print(f"Dealer busts!")
    elif player_score == dealer_score:
        print(f"The player and the dealer tied!")
    elif(player_score > dealer_score):
        print(f"You win with a {game_state['Player']['status']}!")
    else:
        print(f"The dealer won with a {game_state['Dealer']['status']}.")    

    play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if play_again != 'y' or play_again != 'n':
        play_again = input("You typed something wrong! Type 'y' or 'n' to play again: ").lower()
    else:
        os.system("CLS")
        print(logo)

