from turtle import *
from snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
from GameOver import GameOver
import time
import os

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("yellow")
screen.title("MySnakeGame")

score_board = ScoreBoard()


snake = Snake()
snake_food = Food()


gameover = GameOver()
screen.tracer(0)

screen.listen()
screen.onkey(fun=snake.move_up, key='w')
screen.onkey(fun=snake.turn_right, key='d')
screen.onkey(fun=snake.turn_left, key='a')
screen.onkey(fun=snake.move_down, key='s')
active_game = True

while True:
    screen.update()
    if not active_game:
        break
    time.sleep(0.15)
    snake.move_in_direction()
    if snake.detect_collision_with_Food(snake_food):
        snake.add_node_to_tail(True)
        snake_food.appear_food(True)
        score_board.increase_score()
    if snake.detect_collision_with_tail():
        print("Collistion with tail")
        snake_food.food.clear()
        gameover.print_gameover()
        active_game = False
    elif snake.detect_collistion_with_wall():
        print("Collision with wall")
        gameover.print_gameover()
        snake_food.food.clear()
        active_game = False
screen.exitonclick()
