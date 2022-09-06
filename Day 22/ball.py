from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.spawn_ball()
        self.set_direction()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def get_move_speed(self) -> float:
        return self.move_speed
        
    def spawn_ball(self):
        self.shape("square")
        self.color("white")
        self.turtlesize(1,1)
        self.penup()
        
    def reset_ball(self):
        self.hideturtle()
        self.move_speed = 0.1
        self.bounce_x()
        self.goto(0,0)
        self.showturtle()

    
    def speed_up(self):
        self.move_speed *= 0.9
    
    def set_direction(self):
        self.setheading(0)

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):        
        self.y_move *= -1
            
    def bounce_x(self):
        self.x_move *= -1
        self.speed_up()
        