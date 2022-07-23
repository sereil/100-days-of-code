#Password Generator Project

#Day 6 of 100 Days of Code

#Sereil-Vann Phlek - 2022-07-23 (1:38 AM)

#Code used in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def follow_wall():
    turn_right()
    move()
 
while front_is_clear():
    move()  

while not at_goal():
    if right_is_clear():
        follow_wall()
    elif front_is_clear():
        move()
    else:
        turn_left()