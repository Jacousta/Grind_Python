from turtle import *
from ball import Ball
from score import Score
import time

score = Score()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
positions = [(-380, -240), (-380, -260), (-380, -280)]

tim = Turtle(shape="square")
tim.color("white")
tim.shapesize(5, 1)
tim.speed("fastest")
tim.penup()
tim.goto(-380, 0)
score_t = 0

jim = Turtle(shape="square")
jim.color("white")
jim.shapesize(5, 1)
jim.speed("fastest")
jim.penup()
jim.goto(380, 0)
score_j = 0

ball = Ball()


def go_up():
    if -280 <= tim.ycor() <= 250:
        y = tim.ycor()
        tim.sety(y + 10)


def go_down():
    if -250 <= tim.ycor() <= 280:
        y = tim.ycor()
        tim.sety(y - 10)


def go_up_j():
    if -280 <= jim.ycor() <= 250:
        y = jim.ycor()
        jim.sety(y + 10)


def go_down_j():
    if -250 <= jim.ycor() <= 280:
        y = jim.ycor()
        jim.sety(y - 10)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_up_j, "Up")
screen.onkey(go_down_j, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if -280 >= ball.ycor() or ball.ycor() >= 280:
        ball.bounce()
    if (jim.distance(ball) < 50 and ball.xcor() > 350) or (tim.distance(ball) < 50 and ball.xcor() < -350):
        ball.reflect()
    if ball.xcor() > 380:
        score.tim_increase()
        score.update_score()
        ball.reset_pos()
    if ball.xcor() < -380:
        score.jim_increase()
        score.update_score()
        ball.reset_pos()

screen.exitonclick()