
import turtle

#to create screen

scr = turtle.Screen()
scr.title("Drawing by SIR")
scr.bgcolor("#00AAF9")
scr.setup(500,500) #width,height

#to create pen

pen = turtle.Turtle()
pen.color('purple')
pen.shape('turtle')
pen.pensize(2)
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
