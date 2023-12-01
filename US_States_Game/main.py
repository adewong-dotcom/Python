import turtle as t
import pandas as pd
from banner import Banner
import csv

screen = t.Screen()
screen.title("U.S. States Game")
image = "US_States_Game/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

""" def get_mouse_click_coor(x, y):
    print(x, y)
t.onscreenclick(get_mouse_click_coor) """
FONT = ("Arial", 12, "normal")
data = pd.read_csv("US_States_Game/50_states.csv")
possible_guesses = 5
answers = []
all_states = data.state.to_list()
playing = True
state_text = t.Turtle()
state_text.pu()
state_text.hideturtle()

while playing:
    answer_state = t.textinput(f"Guess the State: {len(answers)}/50", "What's a state's name?").title()
    if answer_state == "Exit":
        playing = False
        states_to_learn = [state for state in all_states if state not in answers]

        dict_learn = {"states": states_to_learn}
        df_learn = pd.DataFrame(dict_learn)
        df_learn.to_csv("US_States_Game/learn_states.csv")
    elif answer_state in all_states:
        if answer_state not in answers:
            answers.append(answer_state)
            state = data[data.state == answer_state]
            state_text.goto(int(state.x), int(state.y))
            state_text.write(arg=answer_state, font=FONT, align="center")
        if len(answers) == len(all_states):
            playing = False
    else:
        possible_guesses -= 1
banner = Banner(len(answers))
banner.game_over()

screen.exitonclick() 