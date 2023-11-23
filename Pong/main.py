from turtle import Turtle, Screen, textinput
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from ai import AI
import time

WIDTH = 900
HEIGHT = 600

#Setup background
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("#2E8B57")
screen.title("Python Pong")
screen.tracer(0)

#Create net
net = Turtle()
net.pen(pencolor="#FFFFFF", pensize = 5, pendown= False, speed=10, shown=False)
x = 0
y = -300
net.goto(x, y)

for n in range(0,40):
    if n%2 == 0:
        net.pu()
        y += 15
        net.goto(x, y)
    else:
        net.pd()
        y += 15
        net.goto(x, y)



#Create paddles for player and computer
player_paddle = Paddle("player")
computer_paddle = Paddle("computer")

#Create scoreboard
scoreboard = Scoreboard()
ball = Ball()

getting_input = True

while getting_input:
    num_players = textinput("Number of Players", "Enter the amount of players: ")
    try:
        num_players = int(num_players)
        if num_players == 1 or num_players == 2:
            getting_input = False
    except ValueError:
        print("Invalid input")


#Create AI for computer paddle
if num_players == 1:
    paddle_ai = AI(ball, computer_paddle)


#Paddle movement
if num_players == 2:
    screen.onkey(fun=computer_paddle.up, key= "w" )
    screen.onkey(fun=computer_paddle.down, key="s")
screen.onkey(fun=player_paddle.up, key= "Up" )
screen.onkey(fun=player_paddle.down, key="Down")
screen.listen()

playing = True

while playing:
    
    screen.update()
    paddle_ai.detect_movement()
    time.sleep(0.01)
    ball.move()
    if num_players == 1:
        paddle_ai.detect_movement()

    #Detecting collision with walls
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce()
    
    if ball.xcor() >= 450:
        scoreboard.update_score("player")
        ball.reset_position()

    if ball.xcor() <= -450:
        scoreboard.update_score("computer")
        ball.reset_position()

    if scoreboard.get_score("player")  == 20 or scoreboard.get_score("computer") == 20:
        playing = False

    player_bounce = (ball.distance(player_paddle) <= 55) and (ball.xcor() <= -425)
    computer_bounce = (ball.distance(computer_paddle) <= 55) and (ball.xcor() >= 425)
    if player_bounce or computer_bounce:
        ball.bounce()

if scoreboard.get_score("player")  == 20:
    scoreboard.game_over("player")
else:
    scoreboard.game_over("computer")

screen.exitonclick()
