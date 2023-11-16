import turtle as t
import random
import colorgram as cg

turtle = t.Turtle()
t.colormode(255)

colors = cg.extract('Damien_Hirst.jpg', 30)

turtle.hideturtle()
turtle.speed("fastest")

def color_selector(color_list):
    color = random.choice(color_list)
    rgb = color.rgb
    return rgb

# width = screen.window_width()
# height = screen.window_height()

def drawing_row(column_height):
    start = (75 *5) *-1
    turtle.pu()
    turtle.setposition((start, column_height))
    for c in range(15):
        turtle.pd()
        turtle.pencolor(color_selector(colors))
        turtle.dot(25)
        turtle.pu()
        turtle.forward(50)

def drawing_art():
    start_height = (75 * 5) * -1
    for r in range(15):
        current_height = start_height + (r * 50)
        drawing_row(current_height)

# drawing_row()
drawing_art()

screen = t.Screen()
screen.exitonclick()