from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0.0, 0.0)

    def print_gameover(self):
        self.write("Gameover", align=ALIGNMENT, font=FONT)
