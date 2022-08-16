from turtle import Turtle, Screen
import snake_module
import time

screen = Screen()

screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = snake_module.Snake()

is_playing = True
while is_playing == True:
    screen.update()

    time.sleep(0.1)
    snake.move()
    #is_playing = False



screen.exitonclick()


