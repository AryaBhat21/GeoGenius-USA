import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


right_ans = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess = []

while len(guess) < 50:
    answer = screen.textinput(title=f"{len(guess)}/50", prompt="What's another state namely?").title()
    #learning
    if answer == "Exit":
        missed = []
        for state in all_states:
            if state not in guess:
                missed.append(state)
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        break

    #if ans state is 1 of the state in all state of data
        #if user is right:
            #create a turtle write name of the state at state's x n y coor
    if answer in all_states:
        guess.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer]
        t.goto(state.x.item(), state.y.item())
        t.write(answer)
#turtle.mainloop()
screen.exitonclick()