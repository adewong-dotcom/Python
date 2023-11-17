import turtle as t
import random

turtles = []
COLORS = ["red", "orange", "yellow", "green", "blue",  "purple"]
screen = t.Screen()
screen.setup(width=500, height= 400)
width = screen.window_width()
height = screen.window_height()

getting_input = True
while getting_input:
    try:
        user_color= screen.textinput(title="Who will win the race?", prompt= "Enter a color: (red/orange/yellow/green/blue/purple):")
        if COLORS.index(user_color) >= 0:
            getting_input = False
    except ValueError:
        print("Enter a valid input.")
        # user_color= screen.textinput(title="Make your bet", prompt="Choose a valid input: (red/orange/yellow/green/blue/purple): ")

for c in range(6):
    temp_turtle = t.Turtle(shape="turtle")
    temp_turtle.color(COLORS[c])
    temp_turtle.pu()
    turtles.append(temp_turtle)

def random_speed(turtles):
    '''
    Takes a list of Turtle objects and sets them to random speeds and moves them forward
    '''
    for turtle in turtles:
        speed = random.randint(0, 10)
        distance = random.randint(0, 10)
        turtle.speed(speed)
        turtle.forward(distance)

def is_winner(first_turtle, user_turtle):
    '''
    Gets the object of the winning turtle, and the user input to check if it is the winner
    It then prints on the screen a little message to say if they won or lost.
    '''
    global COLORS
    global turtles
    global screen
    index_user = COLORS.index(user_turtle)
    index_winner = turtles.index(first_turtle)
    winner = COLORS[index_winner]
    text = t.Turtle()
    text.hideturtle()
    text.pu()
    text.setposition(0, (height/2-40))
    if index_user == index_winner:
        text.write(arg=f"The {winner} turtle wins! You win!", align="center", font = ("Arial", 18, "normal"))
        return
    text.write(arg=f"The {winner} turtle wins. You lose.", align="center", font = ("Arial", 18, "normal"))

def is_end(turtles):
    ''' 
    Takes a list of Turtle objects and checks if any of them have reached the end
    '''
    global width
    global user_color
    for turtle in turtles:
        location = turtle.xcor()
        if location >= (width/2 - 20):
            is_winner(turtle, user_color)
            return True
    return False

def starting_positions(turtles):
    '''
    Takes list of Turtle objects and puts them on the starting line
    '''
    global width
    global height
    x = (width/2) * -1 +30
    y = (height/2)/2 * -1 +30
    num_turtles = len(turtles)
    for n in range(num_turtles):
        turtles[n].setposition(x, y)
        y += (height/num_turtles)/2

running = True

starting_positions(turtles)
random_speed(turtles)

while running:
    random_speed(turtles)
    if is_end(turtles):
        for t in turtles:
            t.speed(0)
        running = False


screen.exitonclick()