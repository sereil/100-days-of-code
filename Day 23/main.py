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
scoreboard = Scoreboard()
carmanager.spawn_car()
game_is_on = True


for _ in range(1):    
    screen.update()
    carmanager.spawn_car()    
    for _ in range(random.randint(0,3)):
        carmanager.move_cars()    

while game_is_on:
    time.sleep(0.1)
    screen.update()        
    carmanager.move_cars()
    carmanager.spawn_car()
    #Detect Collision with a Car
    for car in carmanager.get_cars():
        if player.distance(car) <= 25:
            print("Player was hit by a car!")
            scoreboard.gameover()
            game_is_on = False
            
    #Detect player crossing finish line
    if player.is_at_finish_line():
        player.level_up()
        scoreboard.update_level()
        carmanager.speed_up_cars()
            
        
        
screen.exitonclick()        
        

    
    