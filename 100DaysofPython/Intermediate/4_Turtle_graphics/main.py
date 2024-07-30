from turtle import Turtle, Screen
from random import Random


tim = Turtle()
random = Random()
# tim.shape("arrow")
# tim.color("black")

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# tim.shape("square")

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.right(angle)
        tim.forward(100)

def line_color():
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor(r, g, b)


for shape_size_n in range(3,11):
    line_color()
    draw_shape(shape_size_n)
    

# for i in range (3,11):
#     sides = 360/i
#     tim.home()
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     tim.pencolor(r, g, b)
#     for _ in range(i):
#         tim.right(sides)
#         tim.forward(100)














screen = Screen()
screen.exitonclick()