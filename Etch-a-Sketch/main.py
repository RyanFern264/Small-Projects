from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")

def move_forward():
    timmy.forward(10)

def turn_counter_clockwise():
    timmy.left(10)

def turn_clockwise():
    timmy.right(10)

def move_backward():
    timmy.back(10)

def clear_game():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="c", fun=clear_game)
screen.exitonclick()