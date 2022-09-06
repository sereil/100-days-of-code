from turtle import Turtle
import time
COUNTDOWN = 3

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
        
    def countdown(self):        
        self.goto(0,0)
        for _ in reversed(range(COUNTDOWN+1)):
            self.clear()
            self.write(_, align="center", font=("Courier", 80,"normal"))
            time.sleep(0.5)
        self.clear()
        
    def update_scoreboard(self):
        #self.countdown()
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 80,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80,"normal"))        
        
    def l_point(self):
        self.l_score +=1
        
    def r_point(self):
        self.r_score +=1