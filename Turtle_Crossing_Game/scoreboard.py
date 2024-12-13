from turtle import Turtle
FONT = ("Courier", 24, "normal")

#class for tracking score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.setposition(-250, 250)
        self.color("black")

    def display(self):
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)