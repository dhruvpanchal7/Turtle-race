from turtle import *
from random import *
'''
c=Turtle()
c.speed(0)
#c.shape('square')
c.penup()
c.goto(-100,200)
for step in range(15):
    c.write(step,align="center")
    c.right(90)
    c.fd(10)
    c.pendown()
    c.fd(160)
    c.penup()
    c.bk(170)
    c.left(90)
    c.fd(20)
'''
d=Turtle(visible=False)
d.penup()
d.goto(200,250)
d.write("Finish Line",align="center")
d.pendown()
d.right(90)
d.forward(300)

bl = Turtle()
bl.color('black')
bl.speed('fastest')
bl.shape('turtle')
bl.penup()
bl.goto(-200,120)
bl.pendown()

r=Turtle()
r.color('red')
r.speed('fastest')
r.shape('turtle')
r.penup()
r.goto(-200,100)
r.pendown()

b=Turtle()
b.color('blue')
b.speed('fastest')
b.shape('turtle')
b.penup()
b.goto(-200,80)
b.pendown()

o=Turtle()
o.color('green')
o.speed('fastest')
o.shape('turtle')
o.penup()
o.goto(-200,60)
o.pendown()

p=Turtle()
p.color('purple')
p.speed('fastest')
p.shape('turtle')
p.penup()
p.goto(-200,40)
p.pendown()

y=Turtle()
y.color('brown')
y.speed('fastest')
y.shape('turtle')
y.penup()
y.goto(-200,20)
y.pendown()

'''
g=Turtle()
g.color('green')
g.shape('turtle')
g.penup()
g.goto(-200,0)
g.pendown()

m=Turtle()
m.speed('fastest')
m.color('magenta')
m.shape('turtle')
m.penup()
m.goto(-200,-20)
m.pendown()
'''

screen = Screen()
'''
for movement in range(110):
    r.forward(randint(1, 6))
    b.forward(randint(1, 6))
    o.forward(randint(1, 6))
    p.forward(randint(1, 6))
    y.forward(randint(1, 6))
'''

while True:
    turtle = choice([bl, r, b, o, p, y])#, g, m])
    turtle.fd(randint(1, 10))
    if turtle.xcor()> 200:
        break

#turtle.color('gold')
turtle.write('         This Turtle Wins')
screen.exitonclick()

