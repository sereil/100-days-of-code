from turtle import Turtle,Screen

turt = Turtle()

screen = Screen()
screen.listen()


def move_forwards():
    turt.forward(10)

def move_backwards():
    turt.backward(10)

def turn_left():
    turt.left(90)

def turn_right():
    turt.right(90)

def shake_screen():
    pos_y = turt.ycor()
    pos_x = turt.xcor()
    direction = turt.heading()
    screen.reset()
    turt.penup()
    turt.hideturtle()
    turt.sety(pos_y)
    turt.setx(pos_x)
    turt.setheading(direction)
    turt.pendown()
    turt.showturtle()

operations={
    "w":move_forwards,
    "s":move_backwards,
    "a":turn_left,
    "d":turn_right,
    "Return":shake_screen
}


print(operations)

for operand in operations:    
    screen.onkey(key=operand,fun=operations[operand])

screen.exitonclick()
