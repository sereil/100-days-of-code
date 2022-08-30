from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()
        self.goto(x=0, y=265)
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)
        self.clear()
    
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER\r\nFINAL SCORE:{self.score}", align=ALIGNMENT, font=FONT)
    

    