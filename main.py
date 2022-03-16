from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_1 = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake_1.up, "Up")
screen.onkey(snake_1.down, "Down")
screen.onkey(snake_1.left, "Left")
screen.onkey(snake_1.right, "Right")


def update_speed():
    if scoreboard.score > 50:
        time.sleep(0.05)
    elif scoreboard.score > 40:
        time.sleep(0.06)
    elif scoreboard.score > 20:
        time.sleep(0.07)
    elif scoreboard.score > 10:
        time.sleep(0.08)
    elif scoreboard.score > 5:
        time.sleep(0.09)
    elif scoreboard.score >= 0:
        time.sleep(0.1)


should_move = True

while should_move:
    screen.update()
    update_speed()

    snake_1.move_snake()

    # Detect Collisions with Food Particles
    if snake_1.head.distance(food) < 15:
        food.refresh_pos()
        snake_1.extend_snake()
        scoreboard.clear_score()

    # Detect Collisions with the Wall
    if snake_1.head.xcor() > 280 or snake_1.head.xcor() < -290:
        snake_1.reset_snake()
        scoreboard.reset_score()
    if snake_1.head.ycor() > 290 or snake_1.head.ycor() < -290:
        snake_1.reset_snake()
        scoreboard.reset_score()

    # Detect Collisions with Tail
    new_segments = snake_1.segments[1:]
    for segment in new_segments:
        if snake_1.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake_1.reset_snake()

screen.exitonclick()
