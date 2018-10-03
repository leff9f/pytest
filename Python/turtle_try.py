import turtle

T = turtle.Turtle()
T.color('green')
T.forward(150)
T.left(90)
T.forward(75)
T.circle(30,360)
i = 0
while i<100:
    T.left(30)
    T.forward(30)
    T.circle(30, 360)
    i+=1
turtle.done()
