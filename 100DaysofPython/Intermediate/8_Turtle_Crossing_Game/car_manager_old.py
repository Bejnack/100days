import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    step = STARTING_MOVE_DISTANCE
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.color(self.random_color())
        self.goto(310,random.randint(-280, 280))
        print(self.step)



    def random_color(self):
        color_randomizer = random.choice(COLORS)
        return color_randomizer

    def car_move(self):
        self.clear()
        speed = self.xcor() - step
        #if self.xcor() > -310:
        self.setx(speed)

    @staticmethod
    def increase_speed():
        step += MOVE_INCREMENT
        


