import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#TODO 6: Setup screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#000000')
screen.title("Snake Game")
screen.tracer(0)


#TODO 9: Level tracker
def level_tracker(score, snake_segments):
    if score < 10:
        for snake in snake_segments:
            snake.speed("slowest")
    elif score >= 10 and score < 15:
        for snake in snake_segments:
            snake.speed("slow")
    elif score >= 15 and score < 20:
        for snake in snake_segments:
            snake.speed("normal")
    elif score >= 20 and score < 25:
        for snake in snake_segments:
            snake.speed("fast")
    else:
        for snake in snake_segments:
            snake.speed("fastest")

#TODO 3: Expand snake when collides with dot

#TODO 5: Detect collision with edge or tail
def is_tail(snake):
    tip = snake.head
    for segment in snake.segments:
        if segment == tip:
            pass
        elif tip.distance(segment) <= 2:
            return True
    return False

def is_edge_screen(snake):
    global screen
    x = snake.head.xcor()
    y = snake.head.ycor()
    x_limit = screen.window_width()/2 - 2
    y_limit = screen.window_height()/2 - 2
    if x >= x_limit or x <= (x_limit *-1):
        return True
    elif y >= y_limit or y <= (y_limit *-1):
        return True
    else:
        return False
def collision_end(snake):
    if is_edge_screen(snake) or is_tail(snake):
        #end game
        return True
    return False
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(fun= snake.left, key="Left")
screen.onkey(fun= snake.right, key="Right")
screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun= snake.down, key="Down")
screen.listen()

playing = True

while playing:
    #level_tracker(score,snake)
    screen.update()
    time.sleep(0.15)

    snake.move()
     
    #Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    if collision_end(snake):
         playing = False


#TODO 7: Print "Game over." after end
scoreboard.game_over()
screen.exitonclick()