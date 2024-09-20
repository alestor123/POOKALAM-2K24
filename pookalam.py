import turtle
import math
# settings
t = turtle.Turtle()
t.speed(0)
outerRadius = 290
innerRadius = 50
def petals(num, length):
    t.pu()
    t.home()
    t.pd()
    t.setheading(0)
    angle = 360 / num
    theta = 0
    t.begin_fill()
    for i in range(num):
        t.setheading(theta)
        t.circle(length)
        theta += angle
    t.end_fill()

# common shapes
def drawSquare(radius,color,degree=0) :
# since diagonal of square is side x √2 
    sideLength = radius * math.sqrt(2)  
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(-sideLength/2, sideLength/2)
    t.pendown()
    for _ in range(4):
        t.backward(sideLength)
        t.left(90)
    t.end_fill()


# border (DRAWING CIRCLE)
t.fillcolor("magenta")
t.begin_fill()
t.pu()
t.goto(0, -50) 
t.pd()
t.circle(innerRadius,360)
t.end_fill()
# inner circle



t.pu()
t.left(90)
t.goto(outerRadius, 0)
t.pd()
t.pendown()
t.circle(outerRadius,360)

# t.fillcolor("dark blue")
# t.begin_fill()
# t.end_fill()

# outer lining :
t.fillcolor("maroon")
t.begin_fill()

t.pu()
t.left(360)
t.goto(outerRadius+10, 0)
t.pd()
t.pendown()
t.circle(outerRadius+10,360)
# outer circle :

t.pu()
t.left(360)
t.goto(outerRadius+15, 0)
t.pd()
t.pendown()
t.circle(outerRadius+15,360)
t.end_fill()
petals(5,innerRadius)

# t.home()

# drawSquare(outerRadius,"magenta")





turtle.exitonclick()


