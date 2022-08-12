from turtle import Turtle, Screen, exitonclick
#####Turtle Intro######

# import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

######## Challenge 1 - Draw a Square ############

# donatello = Turtle()
# donatello.shape ("turtle")
# donatello.color("orange")

# screen = Screen()
# for _ in range(0,4):
#     donatello.right(90)
#     donatello.forward(100)

# screen.exitonclick()

########### Challenge 2 - Draw a Dashed Line ########

# import turtle as t

# cursor = t.Turtle()

# cursor.shape("arrow")

# screen = t.Screen()
# for _ in range(10):
#     cursor.forward(10)
#     cursor.penup()
#     cursor.forward(10)
#     cursor.pendown()
# screen = exitonclick()

########### Challenge 3 - Draw Shapes ########

# import turtle as t
# import random
# tim = t.Turtle()

# screen = t.Screen()
# screen.colormode(255)
# for sides in range (4,9):
#     r_val = random.randint(0,255)
#     g_val = random.randint(0,255)
#     b_val = random.randint(0,255)
#     tim.pencolor(r_val, g_val, b_val)
#     for _ in range(sides):
#         tim.forward(90)
#         tim.right(360/sides)
# screen.exitonclick()
    

########### Challenge 4 - Random Walk ########
# import turtle as t
# import random

# tim = t.Turtle()
# screen = t.Screen()
# tim.pensize(10)
# tim.shape("classic")
# tim.hideturtle()
# tim.speed("fastest")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# for _ in range (201):
#     tim.setheading(random.choice(directions))
#     tim.color(random.choice(colours))    
#     tim.forward(35)
# screen.exitonclick()

########### Challenge 5 - Spirograph ########

'''https://aperiodical.com/2021/12/the-mathematics-of-spirograph/'''
import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        radius = 80
        tim.color(random_color())
        tim.circle(radius)
        tim.left(radius / size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()