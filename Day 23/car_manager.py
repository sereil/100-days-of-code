from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self) -> None:        
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def get_cars(self):
        return self.cars
    
    def spawn_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
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
            self.cars.append(new_car)

    def speed_up_cars(self):
        self.car_speed += MOVE_INCREMENT
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
    
    