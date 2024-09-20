import turtle
import math
# settings
t = turtle.Turtle()
outerRadius = 300
innerRadius = 50


# border 
t.begin_fill()
t.circle(innerRadius,360)
t.pu()
t.left(90)
t.goto(outerRadius, 0)
t.pd()
t.circle(outerRadius,360)

turtle.exitonclick()
