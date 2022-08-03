

#Print Logo

#Select Two Options, Print them:
#"X" has follower count of 'n', "Y" has 'Higher' or 'Lower' follower count.

#Compare Followers

#Check if user entered right or wrong

#Update Score

#Keep Playing?
#High Score?

from art import logo, vs
import random
import os
import game_data

data = game_data.data
score = 0

def clear():
    os.system("CLS")
    
def choose_influencer(dataset):
    return random.choice(dataset)    

def format_data(account):
    """Takes the account data and returns the printable format."""
    acc_name = account["name"]
    acc_country = account["country"]
    acc_description = account["description"]
    return f"{acc_name}, a {acc_description}, from {acc_country}"   

    
def is_winner(guess, account_a, account_b):
    """Take the user guess and follower acounts and return if they got it right."""
    accA_followers = account_a["follower_count"]
    accB_followers = account_b["follower_count"]
    
    """If account with highest follower AND guess was correct, return true."""
    if accA_followers > accB_followers:
        return guess == "a"
    elif accB_followers > accA_followers:
        return guess == "b"
    else:
        print("Unexpected answer. Exiting game.")
        exit

def game(score,previous_influencer):
    clear()
    print(logo)
    
    if score > 0:
        print(f"You're right! Current score: {score}.")

    inf1 = previous_influencer
    inf2 = choose_influencer(data)

    if inf1 == inf2:
        inf2 = choose_influencer(data)
    
    print(f"Compare A: {format_data(inf1)}")
    print(vs)
    print(f"Against B: {format_data(inf2)}")
    choice = input("Who has more followers? Choose option 'A' or 'B': ").lower()

    is_correct = is_winner(choice,inf1,inf2)
    if is_correct == True:
        score +=1
        game(score,inf2)
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong.")
        print(f"Final score: {score}")

game(score,choose_influencer(data))
    
