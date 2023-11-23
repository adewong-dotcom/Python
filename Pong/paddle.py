from turtle import Turtle

INITIAL_POSITIONS = ((425, 0), (-425, 0))
DISTANCE = 30

class Paddle(Turtle):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.create_paddle(self.user)

    def create_paddle(self, user):
        self.shape("square")
        self.color("#FF0000")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        if user == "player":
            self.goto(INITIAL_POSITIONS[1])
        else:
            self.goto(INITIAL_POSITIONS[0])
    
    def up(self):
        if self.ycor() <= 245:
            self.forward(DISTANCE)

    def down(self):
        if self.ycor() >= -245:
            self.backward(DISTANCE)
