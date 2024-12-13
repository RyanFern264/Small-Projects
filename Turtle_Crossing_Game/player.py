from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#player turtle class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reposition(self):
        self.setposition(STARTING_POSITION)

    def finish_line_check(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False