# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Screen, Turtle
from random import choice

turtle.colormode(255)


def set_position(x, y):
    canvas.hideturtle()
    canvas.penup()
    canvas.goto(x, y)
    canvas.showturtle()
    canvas.pendown()


def first_position():
    canvas.penup()
    canvas.setheading(200)
    canvas.forward(350)
    canvas.setheading(0)
    return canvas.pos()


canvas = Turtle()
canvas.speed("fastest")
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]
size = 20
row_count = 0
coordinates = first_position()
x_coordinate = coordinates[0]
y_coordinate = coordinates[1]

while row_count < 9:
    for dot in range(14):
        canvas.dot(size, choice(color_list))
        canvas.penup()
        canvas.forward(50)
        canvas.pendown()
    row_count += 1
    set_position(x_coordinate, y_coordinate+50*row_count)

screen = Screen()
screen.exitonclick()
