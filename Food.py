from turtle import *
from random import randint


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.penup()
        self.food.hideturtle()
        self.food.goto(50, 50)
        self.food.begin_fill()
        self.food.dot(10, "red")
        self.food.end_fill()

    def appear_food(self, have_eaten_food):
        if have_eaten_food:
            self.food.clear()
            x_cor = randint(-225, 225)
            y_cor = randint(-225, 225)
            self.food.goto(x_cor, y_cor)
            self.food.begin_fill()
            self.food.dot(10, "red")
            self.food.end_fill()



