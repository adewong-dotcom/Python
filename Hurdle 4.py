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
    if wall_in_front() and not right_is_clear():
        turn_north()
    elif wall_on_right() and is_facing_north():
        move()
    elif right_is_clear() and is_facing_north():
        turn_right()
        move()
        turn_right()
        move()
    else:
        move()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
