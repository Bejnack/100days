from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

paddle = Turtle()
paddle.penup()
paddle.color("white")
paddle.shape("square")
#paddle.resizemode("user")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)


def go_up():
    paddle.sety(paddle.ycor()+20)
def go_down():
    paddle.sety(paddle.ycor()-20)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")



screen.exitonclick()