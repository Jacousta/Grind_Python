from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce(self):
        self.y = self.y * -1

    def reflect(self):
        self.x = self.x * -1
        self.move_speed = self.move_speed * 0.9

    def reset_pos(self):
        self.home()
        self.reflect()
        self.move_speed = 0.1


