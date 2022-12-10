import turtle as t
import colorsys as c

t.bgcolor('black')
t.tracer(15)

h = 20

for circle in range(200):
    color = c.hsv_to_rgb(h, 1, 1)
    h += 0.008
    t.color(color)
    t.pensize(3)
    t.goto(0, 0)
    t.circle(circle)
    t.lt(160)
    t.circle(circle)
    t.lt(160)

t.done
