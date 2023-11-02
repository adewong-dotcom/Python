def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_south():
    turn_right()
    move()
    
loop_repetition = 0

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear() and loop_repetition < 4:
            turn_right()
            loop_repetition += 1
    elif wall_in_front() and wall_on_right():
        turn_left()
        loop_repetition = 0
    elif wall_in_front():
        turn_right()
        loop_repetition += 1
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
