from turtle import *

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.forward(-20)


def move_cout_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clock():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_cout_clock, "a")
screen.onkey(move_clock, "d")
screen.onkey(clear, "c")
screen.exitonclick()
