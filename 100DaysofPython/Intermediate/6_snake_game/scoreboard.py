from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    """_summary_

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score(0)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over!", align=ALIGN, font=FONT)

    def update_score(self, score):
        """_summary_

        Args:
            score (_type_): _description_
        """
        self.clear()
        self.goto(0, 260)
        message = f"Score = {score}"
        self.write(arg=message, align=ALIGN, font=FONT)
