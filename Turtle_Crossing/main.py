from turtle import Screen, Turtle
import time
from player import Player
from cars_generator import CarsGenerator
from scoreboard import Scoreboard
# from PIL import Image, ImageTk
# import tkinter
# import os

WIDTH = 800
HEIGHT = 700
X_LIMIT = WIDTH/2
Y_LIMIT = (HEIGHT-100)/2 -20
LEFT = X_LIMIT * -1
BOTTOM = Y_LIMIT * -1
INITIAL_POSITIONS = [(LEFT, Y_LIMIT), (LEFT, 25), (LEFT, 0), (LEFT, -25), (LEFT, BOTTOM)]
FINAL_POSITIONS = [(X_LIMIT, Y_LIMIT), (X_LIMIT, 25), (X_LIMIT, 0), (X_LIMIT, -25), (X_LIMIT, BOTTOM)]

screen = Screen()
screen.setup(WIDTH, HEIGHT)
file = "/Users/adewong/Desktop/Coding/100 Days of Code/Code4Challenge/Turtle_Crossing/black-texture.gif"
# image = Image.open(file)
# image = image.resize((600, 800))
# image = ImageTk.PhotoImage(image)
# screen.bgpic(os.path.expanduser(file))
time.sleep(0.2)
screen.bgcolor('#696969')
screen.tracer(0)
#screen.mainloop()
stripes = []
for index in range(5):
    new_stripe = Turtle()
    new_stripe.pu()
    if index == 2:
        new_stripe.pen(pencolor='#3CB371', pensize=45, speed=10)
    elif index == 0 or index == 4:
        new_stripe.pen(pencolor='#FFD700', pensize=5, speed=10)
    else:
        new_stripe.pen(pencolor="#F5F5F5", pensize=5, speed=10)
    new_stripe.hideturtle()
    new_stripe.goto(INITIAL_POSITIONS[index])
    new_stripe.pd()
    new_stripe.goto(FINAL_POSITIONS[index])

traffic_space = ((Y_LIMIT*2)-50)/8
x_location = LEFT
y_location = Y_LIMIT
length = WIDTH/24
for index in range(3):
    top_stripe = Turtle()
    bottom_stripe = Turtle()
    top_stripe.pen(pencolor="#F5F5F5", pensize=5, speed=10)
    bottom_stripe.pen(pencolor="#F5F5F5", pensize=5, speed=10)
    top_stripe.hideturtle()
    bottom_stripe.hideturtle()
    top_stripe.pu()
    bottom_stripe.pu()
    y_location -= traffic_space
    top_stripe.goto((x_location, y_location))
    y_location *= -1
    bottom_stripe.goto((x_location, y_location))
    y_location *= -1

    for n in range(48):
        if n%2 == 0:
            top_stripe.pd()
            bottom_stripe.pd()
        else:
            top_stripe.pu()
            bottom_stripe.pu()
        x_location += length
        top_stripe.goto((x_location, y_location))
        y_location *= -1
        bottom_stripe.goto((x_location, y_location))
        y_location *= -1
    x_location = LEFT

#Instantiating Player, Cars, Scoreboard
player = Player()
cars = CarsGenerator()
scoreboard = Scoreboard()

#Player movements
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")
screen.listen()

playing = True

while playing:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.start_traffic()

    if player.ycor() >= Y_LIMIT:
      scoreboard.update()
      time.sleep(0.2)
      player.initial_location()

    if cars.crash(player):
        playing = False
        scoreboard.game_over()


screen.exitonclick()