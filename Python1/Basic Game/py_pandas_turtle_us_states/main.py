import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US state game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer = screen.textinput(title="Guess the state", prompt="Enter the name of the state")
screen.tracer(0)
data = pd.read_csv("50_states.csv")
score = 0
for n in range(len(data["state"])):
    if answer == "exit":
        break
    if answer == (data["state"][n]).lower():
        screen.update()
        jim = turtle.Turtle()
        jim.penup()
        jim.hideturtle()
        jim.setx(int(data["x"][n]))
        jim.sety(int(data["y"][n]))
        jim.write(answer.title(), font=("Monaco", 13, "normal"))
        score = score + 1
        answer = screen.textinput(title=f"Guess the state--  SCORE - {score}", prompt="Enter the name of the state")
    # else:
    #     answer = screen.textinput(title=f"Guess the state", prompt="Enter the name of the state")

screen.exitonclick()
