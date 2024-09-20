import turtle
import math
# settings
t = turtle.Turtle()
t.speed(0)
outerRadius = 300
innerRadius = 50

# common shapes
def drawSquare(radius,color,degree=0) :
# since diagonal of square is side x √2 
    sideLength = radius * math.sqrt(2)  
    t.color('red')
    t.fillcolor(color)
    t.penup()
    t.goto(-sideLength/2, sideLength/2)
    t.pendown()
    for _ in range(4):
        t.backward(sideLength)
        t.left(90)


# border (DRAWING CIRCLE)
t.pu()
t.goto(0, -50) 
t.pd()
t.circle(innerRadius,360)
t.pu()
t.left(90)
t.goto(outerRadius, 0)
t.pd()
t.pendown()
t.circle(outerRadius,360)
drawSquare(outerRadius,"violet")




turtle.exitonclick()


