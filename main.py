from turtle import Turtle, Screen
import turtle as t
import random

color_list = [(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68),
              (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17),
              (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8),
              (223, 141, 208), (11, 97, 62)]

the_turtle = Turtle()
screen = Screen()
the_turtle.hideturtle()
t.colormode(255)
the_turtle.penup()
the_turtle.setpos(-200, -200)
the_turtle.pendown()

for i in range(1, 11):
    position = i * 50
    for j in range(10):
        the_turtle.dot(20, random.choice(color_list))
        the_turtle.penup()
        the_turtle.forward(50)
        the_turtle.pendown()
    the_turtle.penup()
    the_turtle.setpos(-200, -200 + position)
    the_turtle.pendown()

screen.exitonclick()
