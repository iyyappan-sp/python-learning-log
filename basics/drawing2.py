import turtle

scr = turtle.Screen()
scr.title("Square Shape By S.I.R")
scr.bgcolor('#98FC97')
scr.setup(600,600)

"""
pen = turtle.Turtle()
pen.shape('turtle')
pen.pensize(3)
pen.fillcolor('green')
pen.begin_fill()
pen.forward(200)
pen.right(90)
pen.fd(200)
pen.rt(90)
pen.fd(200)
pen.rt(90)
pen.fd(200)
pen.end_fill()
"""
# try in other way

pen = turtle.Turtle()
pen.shape('turtle')
pen.pensize(3)
pen.fillcolor('green')
pen.begin_fill()
for i in range(4):
    pen.fd(200)
    pen.lt(90)
pen.end_fill()

pen.fillcolor('yellow')
pen.begin_fill()
for i in range(4):
    pen.fd(200)
    pen.rt(90)
pen.end_fill()

pen.fillcolor('red')
pen.begin_fill()
for i in range(4):
    pen.fd(-200)
    pen.rt(90)
pen.end_fill()

pen.fillcolor('blue')
pen.begin_fill()
for i in range(4):
    pen.fd(-200)
    pen.lt(90)
pen.end_fill()
