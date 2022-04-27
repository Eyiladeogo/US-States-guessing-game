import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
print(states_list)
guessed_states = []
guess_is_correct = True
while len(guessed_states) < 50 and guess_is_correct:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        t.goto(x_cor, y_cor)
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))
        states_list.remove(answer_state)
    else:
        guess_is_correct = False
        df = pandas.DataFrame(states_list)
        df.to_csv("states_to_learn.csv")

screen.exitonclick()
