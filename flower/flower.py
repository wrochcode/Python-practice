import turtle

turtle.bgcolor('white')
turtle.speed(20)
turtle.hideturtle()

Colors = ['black', 'pink', 'black', 'pink',]

for i in range (180):
    for u in Colors:
        turtle.color(u)
        turtle.circle(200 - i, 100)
        turtle.lt(90)
        turtle.circle(200 - i, 100)
        turtle.end_fill()

turtle.mainloop()        
