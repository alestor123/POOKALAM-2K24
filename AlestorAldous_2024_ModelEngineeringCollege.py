import turtle
import math
# settings
t = turtle.Turtle()
t.speed(0)
outerRadius = 300
innerRadius = 50

# functions for common shapes
def drawCircle(color,radius): 
    t.begin_fill()
    t.fillcolor(color)
    t.pu()
    t.rt(90)
    t.fd(radius)
    t.left(90)
    t.down()
    t.circle(radius)
    t.end_fill()
    t.pu()
    t.home()
    t.down()

def petals(num, length,color="none"):
    t.pu()
    t.home()
    t.pd()
    t.setheading(0)
    angle = 360 / num
    theta = 0
    if color != "none": t.fillcolor(color)
    t.begin_fill()
    for i in range(num):
        t.setheading(theta)
        t.circle(length)
        theta += angle
    t.end_fill()

def coverFlower(color,radius):
    for i in range(13):
        t.up()
        t.goto(0,0)
        t.down()
        t.fillcolor(color)
        t.pen(pencolor=color)
        t.begin_fill()
        t.circle(radius,70)
        t.left(110)
        t.circle(radius,70)
        t.end_fill()
        t.right(1)

drawCircle("navy",outerRadius+10)
drawCircle("#FF8C00",outerRadius)
coverFlower("#FAE033",outerRadius-39)
petals(5,innerRadius+30,"magenta")
drawCircle("yellow",innerRadius)
coverFlower("navy",innerRadius-10)
t.color("gold")
style = ("monospace",15)
t.write("\n FOSS",font=style,align="center")
t.hideturtle()
turtle.exitonclick()


