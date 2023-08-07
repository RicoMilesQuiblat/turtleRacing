from turtle import Turtle, Screen
import random

screen = Screen()
screen_width = screen.window_width() / 2
screen_height = screen.window_height() / 2
print(screen_width)
starting_pos_x = -(screen_width - 100)
color_list = ["red", "blue", "yellow", "green", "black"]
red = Turtle()
blue = Turtle()
yellow = Turtle()
green = Turtle()
black = Turtle()
turtle_list = [red, blue, yellow, green, black]
count = 0
y_offset = 100
choice = screen.textinput("Turtle Racing: ", "What color will win? ")
for turtle in turtle_list:
    turtle.color(color_list[count])
    turtle.shape("turtle")
    turtle.penup()
    turtle.setposition(starting_pos_x, screen_height - y_offset)
    y_offset += 100
    count += 1


def move_forward():
    for t in turtle_list:
        if t.xcor() >= 340:
            return t.pencolor()
        number = random.randint(1, 5)
        t.forward(number)
    return "none"


winner = ""
while True:
    winner = move_forward()
    if winner != "none":
        break

if choice == winner:
    print(f"You win. The winner is {winner}")
else:
    print(f"You lose. The winner is {winner}")
screen.exitonclick()