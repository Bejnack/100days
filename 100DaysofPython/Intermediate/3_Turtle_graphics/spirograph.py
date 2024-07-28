import turtle as t
import random

t.colormode(255)

screen = t.Screen()
beji = t.Turtle()

beji.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

for _ in range (36):
    beji.color(random_color())
    beji.circle(100)
    beji.left(10)

screen.exitonclick()
