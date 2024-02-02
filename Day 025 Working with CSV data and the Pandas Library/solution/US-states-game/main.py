import turtle

import pandas
import pandas as pd
from state_capital import StateCapital

correct_state = []
# set up the screen and the background image
screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# upload the states data
states_data = pd.read_csv("50_states.csv")
# save states in the list
states_list = states_data['state'].tolist()
# get user answer and check if it right
while len(correct_state) < 50:
    title_state = screen.textinput(title=f"{len(correct_state)}/50 Guess the State",
                                   prompt="What's another state's name?").title()
    if title_state == "Exit":
        # find missing state by taking difference between two lists
        missing_state = list(set(states_data['state'].tolist()) - set(correct_state))
        # save missing states in csv file
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    # check if user input exist in states' list
    if title_state in states_list:
        correct_state.append(title_state)
        # remove the right answer from the states' list
        states_list.remove(title_state)
        # get the coordinates
        x = states_data.loc[states_data['state'] == title_state, 'x'].iloc[0]
        y = states_data.loc[states_data['state'] == title_state, 'y'].iloc[0]
        # create new turtle and put the capital name on the map
        new_capital = StateCapital(title_state, x, y)


turtle.mainloop()
