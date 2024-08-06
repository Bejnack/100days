import random
from turtle import Turtle

class Food(Turtle):
    """_summary_

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 ,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        """_summary_
        """
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)
