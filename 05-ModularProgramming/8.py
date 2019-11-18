import turtle

def drawSquare(x,y,n):
    pen = turtle.Turtle()
    pen.penup()
    pen.setposition(x,y)
    pen.pendown()
    for i in range(0, 4):
        pen.forward(n)
        pen.right(90)
    

for i in range(1, 5):
    for j in range(1, 5):
        drawSquare(-300+i*100, 300-j*100, 100)
