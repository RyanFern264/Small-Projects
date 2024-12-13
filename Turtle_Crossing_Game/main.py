import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()
scoreboard.display()
#TODO: create player Turtle and allow movement to top of screen X
#TODO: generate a constant stream of random cars moving right to left X
#TODO: detect player collision with a car X
#TODO: move on to next level when player reaches the end X
#TODO: increase all car speeds on higher levels X
#TODO: track and display player score X

screen.listen()
screen.onkey(player.move, "Up")
car_manager = CarManager()

#main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    if player.finish_line_check():
        player.reposition()
        scoreboard.level_up()
        car_manager.increase_speed(scoreboard.current_level)

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()