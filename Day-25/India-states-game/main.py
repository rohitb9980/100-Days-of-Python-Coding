import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x.iloc[0])
        y_cor = int(state_data.y.iloc[0])

        # Move turtle and write text
        t.goto(x_cor, y_cor)
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))
