import turtle


def draw_flower(num_petals, color, x, y):
  turtle.color(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(50)
  turtle.end_fill()

  for i in range(num_petals):
    turtle.left(360 / num_petals)
    turtle.forward(100)
    turtle.left(180 - (360 / num_petals))
    turtle.forward(100)


draw_flower(6, "red", 0, 0)
draw_flower(8, "orange", 100, 0)
draw_flower(10, "yellow", -100, 0)
draw_flower(12, "green", 0, -100)
draw_flower(14, "blue", 100, -100)
draw_flower(16, "purple", -100, -100)

turtle.exitonclick()
