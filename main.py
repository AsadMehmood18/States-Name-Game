import turtle
import  pandas

IMAGE = "blank_states_img.gif"


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exist":
        missing_states = [state for state in all_states if state not in guessed_states]
        data_dic = {
            "states": missing_states
        }
        data = pandas.DataFrame(data_dic)
        data.to_csv("states_to_learn.csv")
        break

    if  answer_state in all_states:
        guessed_states.append(answer_state)
        location = turtle.Turtle()
        location.hideturtle()
        location.penup()
        state_data = data[data.state == answer_state]
        location.goto(state_data.x.item(), state_data.y.item())
        location.write(answer_state)







