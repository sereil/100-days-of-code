from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

cars = []

class CarManager:
    def __init__(self) -> None:        
        pass
            

    def spawn_car(self):
        new_car = Turtle()
        new_car.penup()        
        new_car.shape("square")
        
        new_car.setheading(180)
        new_car.turtlesize(1,2,1)
        rand_color = random.choice(COLORS)
        new_car.color(rand_color)
        
        rand_x = random.randint(280,300)
        rand_y = random.randint(-230,280)
        new_car.goto(rand_x,rand_y)
        cars.append(new_car)

    def move_cars(self):
        for car in cars:
            car.forward(10)
            if car.xcor() <= -293 and car.xcor() >= -300:
                self.spawn_car()
    
    