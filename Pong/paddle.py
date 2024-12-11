from turtle import Turtle
MOVE_DISTANCE = 30

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.setposition(x=xcor, y=ycor)
        self.score = 0

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)