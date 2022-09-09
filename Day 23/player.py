from turtle import Turtle, Screen
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.movement()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def movement(self):
        screen = Screen()
        screen.listen()
        screen.onkey(fun=self.move_forward, key="w")
        screen.onkey(fun=self.move_forward, key="Up")

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y            

    def level_up(self):
        self.goto(STARTING_POSITION)
        