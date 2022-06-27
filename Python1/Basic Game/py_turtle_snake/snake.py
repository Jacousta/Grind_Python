from turtle import *

positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __int__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for n in positions:
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(n)
            self.segments.append(tim)
    #
    # def move(self):
    #     for n in range(len(self.segments), 0, -1):
    #         new_position = self.segments[n - 1].pos()
    #         self.segments[n].goto(new_position)
    #     self.segments[0].forward(20)
