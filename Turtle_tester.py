import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

turtle.shape("turtle")
colors = ["dim gray", "steel blue", "dark turquoise", "cadet blue", "pale goldenrod", "gold", "lime green", "misty rose",
          "olive drab", "dark orange", "firebrick", "light salmon", "orange red", "red", "blue", "crimson", "yellow",
          "green", "purple", "salmon", "light coral", "rosy brown", "orchid", "medium purple", "medium slate blue", "lavender"]
turtle.color("red")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def draw_square():
    for _ in range(4):
        turtle.right(90)
        turtle.forward(100)

def dashed_line():
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_shape(sides):
    angle = 360/sides
    #turtle.pencolor(random.choice(colors))
    turtle.pencolor(random_color())
    for _ in range(sides):
        turtle.right(angle)
        turtle.forward(100)

def random_walk(num):
    turtle.hideturtle()
    turtle.pensize(5)
    directions = [turtle.forward, turtle.backward, turtle.right, turtle.left]
    while num > 0:
        #turtle.pencolor(random.choice(colors))
        turtle.pencolor(random_color())
        direction = random.randint(0,3)
        move = directions[direction]
        if direction == 0 or direction == 1:
            move(20)
        else:
            move(90)
        num -= 1

def spirograph(gap):
    turtle.hideturtle()
    turtle.speed("fastest")
    for n in range(int(360/gap)):
        position = turtle.heading()+gap
        turtle.setheading(position)
        turtle.pencolor(random_color())
        turtle.circle(100)
        

# random_walk(300)
spirograph(5)

screen = t.Screen()
screen.exitonclick()