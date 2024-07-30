from turtle import Turtle, Screen
from random import Random
import random


tim = Turtle()
random = Random()
tim.pensize(10)

def line_color():
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor(r, g, b)

def walk(steps):
    direction = ['fd', 'bw', 'lt', 'rt']
    for _ in range(steps):
        line_color()
        sel_direction = random.choice(direction)
        print(f"selected direction = {sel_direction}")
        if sel_direction == 'fd':
            tim.forward(20)
            print("a")
        elif sel_direction == 'bw':
            tim.backward(20)
            print("b")
        elif sel_direction == 'lt':
            tim.left(90)
            tim.forward(20)
            print("c")
        else:
            tim.right(90)
            tim.forward(20)
            print("d")

walk(100)
















screen = Screen()
screen.exitonclick()