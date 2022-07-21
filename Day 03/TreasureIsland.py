#TreasureIsland

#Day 3 of 100 Days of Code

#Sereil-Vann Phlek - 2022-07-19

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
input1 = """You wander into a temple on Treasure Island, the first room has two doors on either side, which do you pick? 
Left or Right."""
success1=""

input2 = """You enter the second room. Ahead of you is a large pool of water with lily pads scattered throughout.
Beyond the water is a door, your only way forward. You must swim or jump across the lily pads to make it through.
Swim or Jump?"""
success2 = "With agility you never knew you had, you jump on top of the lily pads and make it all the way to the door. Parkour!"

input3 = """You open the door, in fronrt of you lays three choices. A red door, a yellow door, and a blue door. Which do you choose?"""

choice1 = input(input1).lower()

if choice1 == "left":
    choice2 = input(input2).lower()
    if choice2 == "jump":
        print(success2)
        choice3 = input(input3).lower()
        if choice3 == "red":
            print("""It's a trap! You open the door and a jet of flames surges at you.
            GAME OVER""")
        elif choice3 == "blue":
            print("""As you open the door, the smell of death wafts over you along a dozen hideous beasts who eat you.
            GAME OVER""")
        elif choice3 == "yellow":
            print("You win!")
        else:
            print ("GAME OVER")
    else:
        print("""As you swim, you feel a tug at your leg. You look, behind you is a swarm of vicious, hungry trouts! 
        You are unable to defend yourself against this many fish.
        GAME OVER""")

else:
    print("""You've fallen into a hole with no way to get back up!
    GAME OVER""")

