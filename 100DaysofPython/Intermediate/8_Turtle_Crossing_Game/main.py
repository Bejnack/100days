import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

#car_manager = CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

car_list = []
car_generation_counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Generate cars and move
    if car_generation_counter == 7:
        car_manager = CarManager()
        car_list.append(car_manager)
        car_generation_counter = 0
    for car in car_list:
        car.car_move()
        if car.distance(player) < 24:
            game_is_on = False
    car_generation_counter += 1
    
    #Finish line
    if player.finished_level():
        scoreboard.score_level_cleared()
        car_manager.increase_speed()
    
screen.exitonclick()
