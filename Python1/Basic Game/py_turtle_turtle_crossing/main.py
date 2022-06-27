import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager


score = 1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TURTLE CROSSING")

tim = Player()
car = CarManager()

screen.listen()
screen.onkey(tim.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car.create_car()
    car.move()
    for cars in car.new_cars:
        if cars.distance(tim) < 20:
            game_is_on = False
            kim = Turtle()
            kim.hideturtle()
            kim.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    if tim.finish_line():
        tim.reset_POS()
        car.level_up()
        score = score + 1

    jim = Turtle()
    jim.hideturtle()
    jim.penup()
    jim.color("black")
    jim.goto(-280, 250)
    jim.write(f"Level {score}", align="left", font=("Courier", 30, "normal"))
    jim.clear()

screen.exitonclick()
