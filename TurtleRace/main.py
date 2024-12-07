from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
                                               "(red, orange, yellow, green, blue, purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
starting_posi = [-230, 90]
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.goto(x=starting_posi[0], y=starting_posi[1])
    starting_posi[1] -= 20
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    i = 0
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            print(user_bet)
            print(colors[i])
            if user_bet == colors[i]:
                print("You won!")
                is_race_on = False
            else:
                print("You lost.")
                is_race_on = False
        i += 1





screen.exitonclick()