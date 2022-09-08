import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()

carmanager.spawn_car()
game_is_on = True


for _ in range(30):    
    screen.update()
    carmanager.spawn_car()    
    for _ in range(random.randint(0,3)):
        carmanager.move_cars()    

while game_is_on:
    time.sleep(0.1)
    screen.update()        
    carmanager.move_cars()
    
    