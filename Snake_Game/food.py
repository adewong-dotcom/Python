import turtle as t
import random

class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('light salmon')
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        location = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(location)