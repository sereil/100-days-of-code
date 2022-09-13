from turtle import Screen
import snake_module
import time
from food_module import Food
from scoreboard import Scoreboard

screen = Screen()

screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = snake_module.Snake()
food = Food()
sb = Scoreboard()


is_playing = True
while is_playing == True:
    screen.update()
    sb.update_scoreboard()

    time.sleep(0.1)
    snake.move()
    #is_playing = False
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        print("Yummy Yummy in my tummy")
        food.refresh()
        sb.increase_score()
        snake.increase_length()

    #Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() <-300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        sb.reset()
        snake.reset()

    #Detect collision with tail.
    for block in snake.snake[1::]:
        if snake.head.distance(block) < 20:
            sb.reset() 
            snake.reset()
            

screen.exitonclick()


