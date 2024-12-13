from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#class for car actions
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.speed_increase = 0
        self.car_chance = 20

    def generate_car(self):
        if random.randint(1, 100) < self.car_chance: # % chance to control generated cars. Scales with speed.
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            self.car_list.append(car)
            self.car_list[-1].setposition(x=350, y=random.randint(-250, 250)) #Should have just changed position then appended, same thing though

    def move_cars(self):
        car_out_of_bounds = False
        for i in range(0, (len(self.car_list))-1):
            self.car_list[i].forward(STARTING_MOVE_DISTANCE + self.speed_increase)
            if self.car_list[i].xcor() < -400:
                car_out_of_bounds = True #detecting as a boolean since trying to pop an OOB car while iterating causes index error
        if car_out_of_bounds:
                self.car_list.pop(0)


    def increase_speed(self, current_level):
        self.speed_increase = MOVE_INCREMENT * current_level+1
        self.car_chance += 10 #increasing speed without increasing car frequency just makes the game easier imo
