from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:\n"
                                                           "(Red, Orange, Yellow, Green, Blue or Purple)")
turtle_name = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    selected_color = random.choice(colors)
    colors.remove(selected_color)
    new_turtle.color(selected_color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_name.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_name:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.speed("slowest")
        random_distance = random.randint(0, 50)
        turtle.forward(random_distance)

screen.exitonclick()
