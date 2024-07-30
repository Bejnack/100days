from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """_summary_
    """
    tim.forward(10)

def move_backwards():
    """_summary_
    """
    tim.backward(10)

def rotate_clockwise():
    """_summary_
    """
    tim.right(10)

def rotate_counterclockwise():
    """_summary_
    """
    tim.left(10)

def clear_screen():
    """_summary_
    """
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
