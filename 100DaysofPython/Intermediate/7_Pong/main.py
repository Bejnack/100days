from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detect collision
    if ball.ycor() >= 285 or ball.ycor() < -285:
        ball.bounce_y()


#colision with r_paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() >= 325 or ball.distance(l_paddle) < 60 and ball.xcor() <= -325:
        ball.bounce_x()


        
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

        
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()


screen.exitonclick()