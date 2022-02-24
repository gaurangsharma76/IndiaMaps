import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("India States and Union Territories Game")

tur=turtle.Turtle()
image = "India-Maps.gif"
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.addshape(image)
tur.hideturtle()
turtle.shape(image)
tur.penup()
file = pd.read_csv("Indian_states.csv")
all_states = file.state.to_list()
print(all_states)
end_game=False
guessed_state=[]
while not end_game:

    answer_state = screen.textinput(title= f"{len(guessed_state)}/{len(all_states)} guessed",prompt="Input the name "
                                                                                                    "of "
                                                                                                    "state").title()

    if answer_state in all_states:
        guessed_state.append(answer_state)
        file_req = file[file['state'] == answer_state]
        tur.goto(int(file_req.x), int(file_req.y))
        tur.write(answer_state)
        if len(guessed_state) == len(all_states):
            end_game = True

    if answer_state == "Exit":
        end_game = True


screen.exitonclick()

