from turtle import Turtle
from turtle import penup
from turtle import color
from turtle import shape
from turtle import goto


class Snake:
    def __init__(self):
        head = Turtle()
        head.penup()
        head.shape("square")
        self.tail = []
        self.tail.append(head)
        self.direction = "right"

    def add_node_to_tail(self, have_eaten_food) -> object:
        if have_eaten_food:
            node = Turtle()
            node.penup()
            node.shape("square")
            n = len(self.tail)
            if self.direction == "up":
                y_cor = self.tail[n - 1].ycor() - 21
                x_cor = self.tail[n - 1].xcor()
            elif self.direction == "right":
                y_cor = self.tail[n - 1].ycor()
                x_cor = self.tail[n - 1].xcor() - 21
            elif self.direction == "left":
                y_cor = self.tail[n - 1].ycor()
                x_cor = self.tail[n - 1].xcor() + 21
            else:
                y_cor = self.tail[n - 1].ycor() + 21
                x_cor = self.tail[n - 1].xcor()
            node.goto(x_cor, y_cor)
            self.tail.append(node)

    def move_in_direction(self):
        temp_pos1 = self.tail[0].position()
        self.tail[0].forward(21)
        temp_pos2 = temp_pos1
        for i in range(1, len(self.tail)):
            temp_pos1 = self.tail[i].pos()
            self.tail[i].setpos(temp_pos2)
            temp_pos2 = temp_pos1

    def move_up(self):
        if self.direction == "right" or self.direction == "left":
            self.direction = "up"
            self.tail[0].setheading(90)

    def move_down(self):
        if  self.direction == "right" or self.direction == "left":
            self.direction = "down"
            self.tail[0].setheading(270)

    def turn_right(self):
        if self.direction == "up" or self.direction == "down":
            self.direction = "right"
            self.tail[0].setheading(0)

    def turn_left(self):
        if  self.direction == "up" or self.direction == "down":
            self.direction = "left"
            self.tail[0].setheading(180)

    def detect_collision_with_tail(self):
        for i in range(1, len(self.tail)):
            if self.tail[0].distance(self.tail[i]) < 20:
                return True
        return False

    def detect_collistion_with_wall(self):
        if self.tail[0].xcor() >= 240 or self.tail[0].xcor() <= -240 or self.tail[0].ycor() >= 240 or self.tail[
            0].ycor() <= -240:
            return True
        return False

    def detect_collision_with_Food(self, snake_food):
        if self.tail[0].distance(snake_food.food) <= 15:
            return True
        return False
