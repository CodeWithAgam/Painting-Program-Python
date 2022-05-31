# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from random import choice
import turtle

# Seting up the turtle from the Turtle Class
t = turtle.Turtle()
t.speed(0)
t.shape("circle")
turtle.colormode(255)

# Colors Required
color_list = [(188, 19, 46), (243, 232, 66), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187), (87, 24, 56), (115, 119, 152), (91, 24, 21)]


t.penup()
t.setheading(270)
t.forward(350)
t.setheading(180)
t.forward(220)
t.setheading(0)
t.pendown()

num_dots = 150

def draw():
    for dot in range(1, num_dots + 1):
        color = choice(color_list)
        t.dot(20, (color[0], color[1], color[2]))
        t.penup()
        t.forward(50)
        t.pendown()

        if dot % 10 == 0:
            t.penup()
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)
            t.pendown()
        
        t.hideturtle()


draw()

# Keep the window open
s = turtle.Screen()
s.title("Python Painting Program")
s.exitonclick()