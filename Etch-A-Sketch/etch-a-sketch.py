import turtle as t

turtle = t.Turtle()
turtle.shape("arrow")
screen = t.Screen()
screen.title("Pythonista Etch-A-Sketch")

def move_forwards():
    turtle.forward(10)
def move_backwards():
    turtle.backward(10)
def clockwise():
    turtle.left(10)
def counter_clockwise():
    turtle.right(10)
def clear():
    turtle.clear()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key = "a", fun=clockwise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.onkey(key='Up', fun=move_forwards)
screen.onkey(key='Down', fun=move_backwards)
screen.onkey(key = 'Left', fun=clockwise)
screen.onkey(key='Right', fun=counter_clockwise)

screen.exitonclick()