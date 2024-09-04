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
car_manager = CarManager()

#car_manager = CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create car
    car_manager.create_car()
    car_manager.move_car()
    
    for car in car_manager.all_cars:
        if car.distance(player) <20:
            game_is_on = scoreboard.game_over()
    #Finish line
    if player.finished_level():
        scoreboard.score_level_cleared()
        car_manager.level_up()
        

screen.exitonclick()
