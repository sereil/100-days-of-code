from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL_LOCATION = (-290, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_num = 1
        self.goto(LEVEL_LOCATION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level_num}",align="left", font=FONT)
        
    def update_level(self):
        self.level_num +=1
        self.update_scoreboard()
        
    def gameover(self):
        self.update_scoreboard()        
        self.goto(0,0)
        self.write("GAMEOVER", align="center",font=FONT)