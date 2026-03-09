import turtle, manager

import pandas

IMG_PATH = "blank_states_img.gif"
DATA_PATH = "50_states.csv"

df = pandas.read_csv(DATA_PATH)
state_list = df["state"].to_list()

screen = turtle.Screen()
screen.addshape(IMG_PATH)
screen.title("US States Game")
turtle.shape(IMG_PATH)
manager = manager.Manager()

is_game_on = True
while is_game_on:
    user_answer = turtle.textinput("Guess the state name.", "What is another State name?").title()
    if user_answer == "Exit":
        break

    is_correct = manager.is_valid_name(user_answer)
    if is_correct:
        manager.make_state(user_answer,manager.get_states_pos(user_answer))
        state_list.remove(user_answer)
    else:
        is_game_on = False

states = pandas.Series(state_list)
states.to_csv("a.csv")