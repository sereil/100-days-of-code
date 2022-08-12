import turtle as t
import colorgram
import os
import random
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

rgb_colors = []
colors = colorgram.extract(f"{ROOT_DIR}\\image.jpg", 30)
for color in colors:
    sum = color.rgb.r+color.rgb.g+color.rgb.b
    if sum < 700:
        rgb_colors.append(color.rgb)


size = 20
scr_size = 900
donatello = t.Turtle()
donatello.speed("fastest")
donatello.pensize(size)
screen = t.Screen()
screen.colormode(255)
screen.screensize(scr_size,scr_size)
screen.setworldcoordinates(-15,-15, screen.window_width(), screen.window_height())

donatello.setposition(0,0)
donatello.penup()
for _ in range(int(scr_size ** 2/50)):
    donatello.dot(size, random.choice(rgb_colors))
    donatello.forward(50)
    if donatello.xcor() >= scr_size:
        donatello.setx(0)
        donatello.sety(donatello.ycor()+50)

screen.exitonclick()
