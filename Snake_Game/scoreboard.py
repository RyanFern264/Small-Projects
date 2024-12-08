from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.color("white")
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.score += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)