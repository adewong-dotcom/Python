from turtle import Turtle
import random

POSITION = (0,0)
DISTANCE = 5
ANGLES = [30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.angle = random.choice(ANGLES)
        self.move()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_len= 1, stretch_wid=1)
        self.speed("slowest")
        self.goto(POSITION)

    def reset_position(self):
        self.goto(POSITION)
        self.angle = random.choice(ANGLES)

    def move(self):
        self.setheading(self.angle)
        self.forward(DISTANCE)
        
    def bounce(self):
        if self.angle+90 > 360:
            self.angle = (self.angle+90) - 360
        else:
            self.angle += 90
        self.setheading(self.angle)