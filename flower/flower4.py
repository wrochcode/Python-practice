import turtle as turtle
import colorsys as colorsys

turtle.setup(600, 600)
turtle.speed(0)
turtle.tracer(100)
turtle.width(2)
turtle.screensize(100)
turtle.bgcolor('black')
for j in range(25):
    for i in range(15):
        turtle.color(colorsys.hsv_to_rgb(i/15, j/25, 1))
        turtle.right(90)
        turtle.circle(200 - j * 4, 90)
        turtle.left(90)
        turtle.circle(200 - j * 4, 90)
        turtle.right(180)
        turtle.circle(2, 54)
        turtle.hideturtle
turtle.done
