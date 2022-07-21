#RockPaperScissors

#Day 4 of 100 Days of Code

#Sereil-Vann Phlek - 2022-07-20

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock Paper Scissors, you will be competing against "'Bob'".")

rps = [rock, paper, scissors]

player_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

bob_rps = random.randint(0,2)

bobs_hand = rps[bob_rps]
players_hand = rps[player_rps]

print("Rock Papers Scissors!")
print(f"Bob's hand: {bobs_hand} Your hand:{players_hand}")


if player_rps > bob_rps:
    if player_rps == 2 and bob_rps == 0:
        print("You lose!")
    else:
        print("You win!")
elif player_rps == 0 and bob_rps == 1:
    print("You win!")
elif player_rps == bob_rps:
    print("It's a draw!")
else:
    print("You lose!")