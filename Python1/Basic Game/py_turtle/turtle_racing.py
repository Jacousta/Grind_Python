from turtle import *
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win? Enter a color")
colors = ["red", "orange", "blue", "green", "black", "brown", "cyan"]
position = [-150.00, -100.00, -50.00, 0.00, 50.00, 100.00, 150.00]
turtle_list = []
winner=[]

for n in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.color(colors[n])
    tim.speed("fastest")
    tim.penup()
    tim.goto(-230, position[n])
    turtle_list.append(tim)
is_on = True
while is_on:
    for n in range(0, 7):
        rand_distance = random.randint(0, 10)
        turtle_list[n].forward(rand_distance)
        if turtle_list[n].xcor() > 230:
            is_on = False
            winner.append(turtle_list[n])
if winner[0].fillcolor() == user_bet:
    print("you win")
else:
    print(f"You loose,{winner[0].fillcolor()} is the winner")


screen.exitonclick()
