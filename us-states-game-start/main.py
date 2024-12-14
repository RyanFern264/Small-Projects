import turtle
from turtle import Turtle

import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True

states_data = pandas.read_csv("50_states.csv")

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Guess another state name")
    answer_state = answer_state.title()
    current_state_data = states_data[states_data["state"] == answer_state]
    if not current_state_data.empty:
        # print(f"{current_state_data}") #full data
        # print(f"{current_state_data.state.iat[0]}") #state name
        # print(f"{current_state_data.x.iat[0]}") #xcor
        # print(f"{current_state_data.y.iat[0]}") #ycor
        text = Turtle()
        text.hideturtle()
        text.penup()
        #text.setposition(x=int(current_state_data.x.iat[0]), y=int(current_state_data.y.iat[0]))
        #alternatively, we can say:
        text.goto(x=int(current_state_data.x.item()), y=int(current_state_data.y.item()))
        #text.write(f"{current_state_data.state.iat[0]}", align="center", font=("Courier", 8, "normal"))
        #again, we can use .item() instead of .iat[0]. .item() looks way cleaner
        text.write(f"{current_state_data.state.item()}", align="center", font=("Courier", 8, "normal"))
screen.exitonclick()