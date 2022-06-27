from turtle import *
import turtle
import random

rgb_list = [(4, 135, 153), (8, 185, 201), (1, 96, 110), (9, 44, 58), (57, 34, 29), (117, 74, 62), (37, 220, 233), (20, 190, 186), (45, 240, 249), (46, 31, 35), (12, 137, 131), (57, 246, 244), (91, 51, 45), (55, 216, 211), (3, 110, 107), (189, 148, 121), (19, 41, 35), (99, 73, 78), (241, 224, 199), (82, 53, 57), (180, 107, 87), (213, 242, 231), (207, 225, 235), (237, 227, 232), (169, 152, 158), (43, 57, 94), (151, 133, 91), (223, 199, 142), (76, 67, 42), (236, 174, 155)]

no_of_dots = 100
tim = Turtle()
my_screen = Screen()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
for dot_count in range(1, no_of_dots + 1):
    tim.dot(20)
    tim.forward(40)
    tim.pencolor(rgb_list[random.randint(0, 29)])
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)
my_screen.exitonclick()
