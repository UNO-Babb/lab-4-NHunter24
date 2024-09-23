#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS




def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(joe, sides):
    for s in range(sides):
        joe.forward(70)
        joe.right(360/sides)

def fillCorner(leo, corner):
    #draw a big square
    drawSquare(leo, 100)
    filled = int(input("Which corner should be filled? 1=TopLeft, 2=TopRight, 3=BottomLeft, 4=BottomRight."))
    if filled == 1:
        leo.begin_fill()
        drawSquare(leo, 50)
        leo.end_fill()
    elif filled == 2:
        leo.forward(50)
        leo.begin_fill()
        drawSquare(leo, 50)
        leo.end_fill()
    elif filled == 3:
        leo.right(90)
        leo.forward(50)
        leo.left(90)
        leo.begin_fill()
        drawSquare(leo, 50)
        leo.end_fill()
    elif filled == 4:
        leo.up()
        leo.forward(50)
        leo.right(90)
        leo.forward(50)
        leo.left(90)
        leo.down()
        leo.begin_fill()
        drawSquare(leo, 50)
        leo.end_fill()
        

def main():
    myTurtle = turtle.Turtle()
    
    #drawsquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
