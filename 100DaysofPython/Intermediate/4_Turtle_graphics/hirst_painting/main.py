# import colorgram

# colors = colorgram.extract('D:\\100days\\100DaysofPython\\Intermediate\\4_Turtle_graphics\\hirst_painting\\image.jpg', 25)

# rgb_colors =[]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
from turtle import Screen
import random


beji = t.Turtle()
t.colormode(255)
beji.speed('fastest')
beji.penup()
beji.hideturtle()


color_list = [
    (199, 175, 117),
    (124, 36, 24),
    (210, 221, 213),
    (168, 106, 57),
    (222, 224, 227),
    (186, 158, 53),
    (6, 57, 83),
    (109, 67, 85),
    (113, 161, 175),
    (22, 122, 174),
    (64, 153, 138),
    (39, 36, 36),
    (76, 40, 48),
    (9, 67, 47),
    (90, 141, 53),
    (181, 96, 79),
    (132, 40, 42),
    (210, 200, 151),
    (141, 171, 155),
    (179, 201, 186),
    (172, 153, 159),
    (212, 183, 177),
    (176, 198, 203),
    ]
# dot(20) --50--> dot

beji.setheading(225)
beji.forward(300)
beji.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    beji.dot(20, random.choice(color_list))
    beji.forward(50)
    beji.dot(20, random.choice(color_list))
    
    if dot_count % 10 == 0:
        beji.setheading(90)
        beji.forward(50)
        beji.setheading(180)
        beji.forward(500)
        beji.setheading(0)




screen = t.Screen()
screen.exitonclick()
