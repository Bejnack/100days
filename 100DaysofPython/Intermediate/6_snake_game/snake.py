"""Snake module
"""
from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """Snake Class
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        """Snake is being created with 3 square bodyparts
        """
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        """Snake movement constant
        """
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        """Snake move up command
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        """Snake move down command
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        """Snake move right command
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        """Snake move left command
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
