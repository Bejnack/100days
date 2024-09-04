from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#define the player class
class Player(Turtle):
    """_summary_
Turtle class to create the player object
    Args:
        Turtle (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.seth(90)
        self.goto(STARTING_POSITION)
        
    def finished_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        
    def go_up(self):
        """_summary_
        move player object up
        """
        self.sety(self.ycor() + MOVE_DISTANCE)
        
    def go_down(self):
        """_summary_
        move player object down
        """
        self.sety(self.ycor() - MOVE_DISTANCE)
