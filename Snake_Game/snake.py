import turtle as t
INITIAL_POSITIONS = [0, -20, -40]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ["cornflower blue", "gold"]

class Snake:
    def __init__(self):
        self.color_alternator = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment((position, 0))

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            self.segments[index].goto(x, y)

        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = t.Turtle(shape="square")
        new_segment.pu()
        new_segment.color(COLORS[self.color_alternator])
        if self.color_alternator == 0:
            self.color_alternator = 1
        else:
            self.color_alternator = 0
        new_segment.goto((position))
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        