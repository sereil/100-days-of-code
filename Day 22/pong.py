from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
#Strange bug where onkeypress Up/Down also controls W and S keys. Need to add an onkeyrelease to offset it...
screen.onkeypress(fun=r_paddle.move_up,key="Up")
screen.onkeypress(fun=r_paddle.move_down,key="Down")
screen.onkeyrelease(fun=None,key="Up")
screen.onkeyrelease(fun=None,key="Down")

screen.onkeypress(fun=l_paddle.move_up,key="w")
screen.onkeypress(fun=l_paddle.move_down,key="s")

ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(ball.get_move_speed())
    screen.update()
    #Detect collision with wall
    if ball.ycor() >= 283 or ball.ycor() <= -283:
        ball.bounce_y()            
    ball.move()
    
    #Detect collision with right paddle
    if (ball.distance(r_paddle) <= 40 and ball.xcor() >= 330) or (ball.distance(l_paddle) <= 40 and ball.xcor() <= -330):
        ball.bounce_x()
    
    #Detect if player scored
    if ball.xcor() >= 390:        
        ball.reset_ball()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    
    if ball.xcor() <= -390:
        ball.reset_ball()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        

    

screen.exitonclick()


