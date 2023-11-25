from turtle import Turtle

WIDTH = 800
HEIGHT = 700
X_LIMIT = WIDTH/2
Y_LIMIT = (HEIGHT-100)/2 -20
LEFT = X_LIMIT * -1
BOTTOM = Y_LIMIT * -1
DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("#006400", "#008000")
        self.pu()
        self.setheading(90)
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.initial_location()
        self.speed("fastest")

    def initial_location(self):
        y_location = BOTTOM - 35
        self.goto(0, y_location)
    
    def up(self):
        if self.ycor() <= (Y_LIMIT+20):
            self.forward(DISTANCE)

    def down(self):
        if self.ycor() >= (BOTTOM - 30):
            self.backward(DISTANCE)