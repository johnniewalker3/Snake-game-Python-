import os.path
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        if os.path.exists("score.txt"):
            with open("score.txt", mode='r') as file:
                self.high_score = int(file.read())
        else:
            with open("score.txt", mode='w') as file:
                file.write(str(self.high_score))

        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.update_score()

    def update_score(self):
        self.clear()
        with open("score.txt", mode='w') as file:
            file.write(str(self.high_score))
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()
