import turtle
import pandas
from scoreboard import Scoreboard

IMAGE = "100-days-of-code\Day 25\\blank_states_img.gif"
data = pandas.read_csv("100-days-of-code\Day 25\\50_states.csv")
all_states = data.state.to_list()
guessed_states = []
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(750, 700)
screen.bgpic(IMAGE)


scoreboard = Scoreboard()

while scoreboard.score < 50:
    answer_state = screen.textinput(title=f"{scoreboard.score}/50 States Correct", prompt="What's another state's name?").title()
   
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("100-days-of-code\Day 25\states_to_learn.csv")
        break
    
    if answer_state in data.values:
        state_data = data[data.state == answer_state]
        scoreboard.increase_score()
        scoreboard.show_state(answer_state, int(state_data.x), int(state_data.y))
        guessed_states.append(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#     state=turtle.textinput("State_Coor_Updater","Which State Did You Click?")
#     state_selected = data[data.state == state]
#     state_selected.x = x
#     state_selected.y = y
    

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
