from turtle import *
from food import Food
from score import Scoreboard
import time


def move_up():
    if segment[0].heading() != 270:
        segment[0].setheading(90)


def move_down():
    if segment[0].heading() != 90:
        segment[0].setheading(270)


def move_right():
    if segment[0].heading() != 180:
        segment[0].setheading(0)


def move_left():
    if segment[0].heading() != 0:
        segment[0].setheading(180)


screen = Screen()
food = Food()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("🐍Snake Game🐍")
screen.tracer(0)
positions = [(0, 0), (-20, 0), (-40, 0)]
segment = []
game_is_on = True

for position in positions:
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    tim.speed("slowest")
    tim.goto(position)
    segment.append(tim)

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for n in range(len(segment) - 1, 0, -1):
        new_position = segment[n - 1].pos()
        segment[n].goto(new_position)
    segment[0].forward(20)
    if segment[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        POS = segment[-1].pos()
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.speed("slowest")
        tim.goto(POS)
        segment.append(tim)
    for seg in segment:
        if segment[0] == seg:
            pass
        elif segment[0].distance(seg) < 10:
            game_is_on = False
            score.reset_score()

    if segment[0].xcor() > 280 or segment[0].ycor() > 280 or segment[0].xcor() < -280 or segment[0].ycor() < -280:
        game_is_on = False
        score.reset_score()

screen.exitonclick()
