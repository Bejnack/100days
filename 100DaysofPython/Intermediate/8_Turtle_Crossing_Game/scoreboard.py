from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"Level: {self.score}" ,align="left", font=FONT)
        
    def score_level_cleared(self):
        self.score += 1
        self.update_scoreboard()
