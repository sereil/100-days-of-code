from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")
hs="100-days-of-code\Day 25\highscore.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.highscore = self.read_highscore()
        self.goto(x=0, y=265)
        
    def increase_score(self):
        self.score +=1
        
    def show_state(self,state, x, y):
        self.goto(x=x,y=y)
        self.write(f"{state}", align=ALIGNMENT,font=FONT)
        

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def save_highscore(self):
        with open(file = hs, mode="w") as file:
            file.write(str(self.highscore))
            
    def read_highscore(self):
        with open(file = hs) as file:
            return int(file.read()) # if not None else 0 '''Does not work if the file has nothing or is empty sadly.'''

    

    