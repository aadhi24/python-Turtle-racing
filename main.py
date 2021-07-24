import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(550, 400)
enter = screen.textinput("NIM", "which turtle will win the game? Enter the colour")
colours = ['yellow', "green", 'red', "orange", "purple", "blue"]
index_no = [-70, -40, -10, 20, 50, 80]
all_turtle = []
loop = True
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, index_no[index])
    tim.color(colours[index])
    all_turtle.append(tim)
if enter:
    loop = True
while loop:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            loop = False
            winner = turtle.pencolor()
            if winner == enter:
                print(f"you won the game {winner}")
            else:
                print(f"you lose the game the winner is {winner}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
