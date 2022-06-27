from turtle import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.tim = 0
        self.jim = 0
        self.goto(-100, 240)
        self.write(self.tim, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 240)
        self.write(self.jim, align="center", font=("Courier", 60, "normal"))

    def tim_increase(self):
        self.tim = self.tim + 1

    def jim_increase(self):
        self.jim = self.jim + 1

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.tim, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 240)
        self.write(self.jim, align="center", font=("Courier", 60, "normal"))
