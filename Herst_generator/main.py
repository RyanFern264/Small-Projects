from random import randint
#import colorgram
#painting_colors = []
#image_colors = colorgram.extract('anime_forest.jpg', 30)
#for i in range(0, len(image_colors)):
#    color_tuple = (image_colors[i].rgb[0], image_colors[i].rgb[1], image_colors[i].rgb[2])
#    painting_colors.append(color_tuple)
#
#print(painting_colors)

from turtle import Turtle, Screen, colormode
from random import random, choice, randint, uniform

screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
color_list = [(29, 49, 62), (114, 96, 62), (65, 104, 87), (200, 163, 87), (48, 104, 120), (35, 56, 48), (230, 213, 107), (158, 149, 66), (59, 51, 39), (105, 189, 159), (241, 234, 171), (76, 161, 141), (43, 76, 64), (34, 77, 83), (53, 162, 178), (78, 198, 209), (56, 48, 52), (73, 73, 39), (100, 230, 243), (134, 221, 190), (189, 234, 192), (87, 68, 72), (79, 57, 52), (73, 58, 62), (40, 63, 91), (155, 243, 248), (191, 106, 78), (177, 95, 104), (185, 136, 142), (108, 127, 154)]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOliveGreen")
timmy.speed("fastest")
colormode(255)
timmy.penup()

def herst_painting():
    for i in range(0, 10):
        for j in range (0,10):
            timmy.dot(20, choice(color_list))
            timmy.forward(50)
            print(timmy.pos())
        timmy.setposition(0, (timmy.pos()[1] + 50))

herst_painting()

screen.exitonclick()