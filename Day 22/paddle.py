from turtle import Turtle, Screen

WIDTH = 20
HEIGHT = 100

PLAYER1KEYS = ("Up","Down")
PLAYER2KEYS = ("W","S")

YPOS = 0

class Paddle(Turtle):
    def __init__(self,pos) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1,outline=1)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.set_paddle_movement()
        self.goto(pos)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(),y=new_y)
        
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(),y=new_y)
        
    
    def set_paddle_movement(self):
        screen = Screen()
        screen.listen()
        screen.onkey(fun=self.move_down,key="Down")
        screen.onkey(fun=self.move_up,key="Up")
        
    
    