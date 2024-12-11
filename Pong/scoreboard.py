from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.color("white")

    def display(self):
        self.write(f"{self.left_score}            {self.right_score}", align="center", font=("Courier", 15, "normal"))

    def left_scored(self):
        self.left_score += 1
        self.clear()
        self.display()

    def right_scored(self):
        self.right_score += 1
        self.clear()
        self.display()