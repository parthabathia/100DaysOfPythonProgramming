import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
us_states = pd.read_csv("50_states.csv")
all_states = us_states["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct.", prompt="Guess a state's name: ").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_states[us_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

states_not_guessed = [state for state in all_states if state not in guessed_states]

df = pd.DataFrame(states_not_guessed)

df.to_csv("states_to_learn.csv")