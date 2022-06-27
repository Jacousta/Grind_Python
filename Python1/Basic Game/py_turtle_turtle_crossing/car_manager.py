from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.new_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 4:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 1.7)
            new_car.goto(300, random.randint(-250, 250))
            self.new_cars.append(new_car)

    def move(self):
        for cars in self.new_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed = self.car_speed + MOVE_INCREMENT
