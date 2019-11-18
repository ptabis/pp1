import turtle

def drawSquare(x,y,n):
    pen = turtle.Turtle()
    pen.penup()
    pen.setposition(x,y)
    pen.pendown()
    for i in range(0, 4):
        pen.forward(n)
        pen.right(90)