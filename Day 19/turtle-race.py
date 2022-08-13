from turtle import Turtle, Screen
import random
from venv import create
screen = Screen()
screen.setup(width=500, height=400)
rainbow = ["purple","blue","green","yellow","orange","red"]



dict_turtles = {}
def create_turtles():
    first_turtle_pos = 180
    for color in rainbow:      
        current_turtle = Turtle(shape="turtle")
        current_turtle.penup()
        current_turtle.color(color)
        current_turtle.goto(-230,first_turtle_pos)
        first_turtle_pos -= 70
        dict_turtles[color] = current_turtle
        print(current_turtle.pencolor())

def move_turtles(lst_turtles):
    race_finished = False
    while not race_finished: 
        for turt in lst_turtles:
            rand_forward = random.randint(1,11)
            this_turtle = dict_turtles[turt]
            this_turtle.forward(rand_forward)
            if this_turtle.xcor() >= 250:
                return this_turtle
        
def verify_bet(winner_color,player_color):
    return winner_color.lower() == player_color.lower()




def start_race():
    create_turtles()
    player_bet = screen.textinput("Choose your turtle", "Which colour do you think will win?").lower()
    winning_turtle = move_turtles(dict_turtles)
    
    if verify_bet(winning_turtle.pencolor(), player_bet):
        print(f"You {player_bet} which won. Congratulations!")
    else:
        print(f"Your turtle did not win, {winning_turtle.pencolor()} was the winner.")

start_race()




screen.exitonclick()