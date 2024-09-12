import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

turtle_write = turtle.Turtle()
turtle_write.penup()
turtle_write.hideturtle()

IMAGE = r"100DaysofPython\Intermediate\10_Weather_Channel\day-25-us-states-game-start\blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)


state_data = pandas.read_csv(r"100DaysofPython\Intermediate\10_Weather_Channel\day-25-us-states-game-start\50_states.csv")
#print(state_data)
state_data_final = state_data.state
state_list = state_data_final.to_list()

correct_guesses = []

game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=f'{len(correct_guesses)}/50 States',prompt=f"What's another state's name?")
    
    
    if answer_state.title() == "Exit":
        #states to learn
        for state in correct_guesses:
            state_list.remove(state)
        states_to_learn = pandas.DataFrame(state_list)#, columns=["colummn"]
        states_to_learn.to_csv(r'100DaysofPython\Intermediate\10_Weather_Channel\day-25-us-states-game-start\states_to_learn.csv')#, index=False
        print(state_list)
        break
    if answer_state.title() in state_list and answer_state.title() not in correct_guesses:
        state_row = state_data[state_data.state == answer_state.title()]
        state_name = state_row.state
        state_xcor = int(state_row.x)
        state_ycor = int(state_row.y)
        turtle_write.goto(state_xcor, state_ycor)
        turtle_write.write(answer_state.title())
        
        correct_guesses.append(answer_state.title())
        
    elif len(correct_guesses) == len(state_list):
        game_is_on = False



#---------------------------------------------------------------------------------------
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
