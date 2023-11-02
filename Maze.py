def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_north():
    turn_left()
def turn_south():
    turn_right()
    move()

going_north = False

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    elif wall_in_front() and wall_on_right():
        turn_north()
    elif wall_in_front():
        turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
