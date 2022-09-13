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
        self.highscore = self.read_highscore()
        self.update_scoreboard()
        self.goto(x=0, y=265)
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT,font=FONT)
        
    
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def save_highscore(self):
        with open(".\highscore.txt", mode="w") as file:
            file.write(str(self.highscore))
            
    def read_highscore(self):
        with open(file=".\highscore.txt") as file:
            return int(file.read()) # if not None else 0 '''Does not work if the file has nothing or is empty sadly.'''

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER\r\nFINAL SCORE:{self.score}", align=ALIGNMENT, font=FONT)
    

    