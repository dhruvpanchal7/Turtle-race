from turtle import*
from random import *

c=Turtle()
c.penup()
c.speed(10000)
c.pendown()
c.circle(110)
c.penup()
c.right(90)
c.forward(160)
c.left(90)
c.pendown()
c.circle(270)
c.left(90)
c.forward(160)
c.penup()

r=Turtle()
r.speed('fastest')
r.color('red')
r.shape('turtle')
r.penup()
r.goto(0,-140)
r.pendown()

b=Turtle()
b.speed('fastest')
b.color('blue')
b.shape('turtle')
b.penup()
b.goto(0,-100)
b.pendown()

o=Turtle()
o.speed('fastest')
o.color('orange')
o.shape('turtle')
o.penup()
o.goto(0,-60)
o.pendown()
p=Turtle()
p.speed('fastest')
p.color('purple')
p.shape('turtle')
p.penup()
p.goto(0,-20)
p.pendown()
'''
y=Turtle()
y.color('yellow')
y.shape('turtle')
y.penup()
y.goto(0,20)
y.pendown()
'''
screen=Screen()
for movement in range(100):
    r.circle(250,randint(1, 6))
    b.circle(210,randint(1, 6))
    o.circle(170,randint(1, 6))
    p.circle(130,randint(1, 6))
    #y.forward(randint(1, 6))


screen.exitonclick()