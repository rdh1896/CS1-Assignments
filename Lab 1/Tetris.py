"""
Name: Russell Harvey
File: Tetris.py / Lab 01
"""

import turtle as tt

def initialize():
    """
    Sets the turtle in a location so that the board
    is more centered on the canvas.
    Pre-Conditions: Turtle is down, facing east.
    Post-Conditions: Turtle is up, facing east. Located at the datum point.
    """
    tt.up()
    tt.fd(-50)
    tt.left(-90)
    tt.fd(100)
    tt.left(90)

def draw_board():
    """
    Draws the outline of Tetris board on the canvas. The dimensions are 100 x 200 units.
    Pre-Conditions: Turtle is up, facing east. Located at the datum point.
    Post-Conditions: Turtle is up, facing east. Located at the datum point.
    """
    tt.down()
    tt.fd(100)
    tt.left(90)
    tt.fd(200)
    tt.left(90)
    tt.fd(100)
    tt.left(90)
    tt.fd(200)
    tt.left(90)
    tt.up()

def draw_block():
    """
    Draws a block that is used to create any of the Tetris shapes. The dimensions are 10 x 10 units.
    Pre-Conditions: Turtle is up, facing east.
    Post-Conditions: Turtle is up, facing east.
    """
    tt.down()
    tt.begin_fill()
    tt.fd(10)
    tt.left(90)
    tt.fd(10)
    tt.left(90)
    tt.fd(10)
    tt.left(90)
    tt.fd(10)
    tt.left(90)
    tt.end_fill()
    tt.up()

def draw_t_shape():
    """
    Draws the "upside down 'T'" Tetris shape on the canvas.
    Pre-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "T shape".
    Post-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "T shape".
    """
    tt.fillcolor("blue")
    draw_block()
    tt.fd(10)
    draw_block()
    tt.left(90)
    tt.fd(10)
    tt.left(-90)
    draw_block()
    tt.fd(10)
    tt.left(-90)
    tt.fd(10)
    tt.left(90)
    draw_block()
    tt.fd(-20)

def draw_square():
    """
    Draws the "sqaure" shaped Tetris block on the canvas.
    Pre-Conditions: Turtle is up, facing east, located on the
    bottom left corner of the "square" shape.
    Post-Conditions: Turtle is up, facing east, located on the
    bottom left corner of the "square" shape.
    """
    tt.fillcolor("red")
    draw_block()
    tt.fd(10)
    draw_block()
    tt.fd(10)
    tt.left(90)
    tt.fd(10)
    draw_block() #Turtle is now facing North
    tt.fd(10)
    tt.left(90)
    tt.fd(10)
    draw_block() #Turtle is now facing West
    tt.left(90)
    tt.fd(20)
    tt.left(-90)
    tt.fd(10)
    tt.left(180)

def draw_l():
    """
    Draws the "L" shaped Tetris block.
    Pre-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "L" shape.
    Post-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "L" shape.
    """
    tt.left(90)
    tt.fd(20)
    tt.left(-90)
    tt.fillcolor("purple")
    draw_block()
    tt.left(-90)
    tt.fd(10)
    tt.left(90)
    draw_block()
    tt.left(-90)
    tt.fd(10)
    tt.left(90)
    draw_block()
    tt.fd(10)
    draw_block()
    tt.fd(-10)

def draw_line():
    """
    Draws the "line" shaped Tetris block.
    Pre-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "line" shape.
    Post-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "line" shape.
    """
    tt.fillcolor("green")
    draw_block()
    tt.left(90)
    tt.fd(10)
    tt.left(-90)
    draw_block()
    tt.left(90)
    tt.fd(10)
    tt.left(-90)
    draw_block()
    tt.left(90)
    tt.fd(10)
    tt.left(-90)
    draw_block()
    tt.left(-90)
    tt.fd(30)
    tt.left(90)

def main():
    """
    Creates the canvas, initializes the turtle location,
    draws the Tetris board, and then creates various
    Tetris shapes in a valid pattern on the board. Asks
    user to close the window to terminate the program.
    """
    initialize()
    draw_board()
    draw_t_shape()
    tt.fd(30)
    draw_square()
    tt.fd(20)
    draw_l()
    tt.fd(20)
    draw_square()
    tt.fd(-10)
    tt.left(90)
    tt.fd(10)
    tt.left(-90)
    draw_line()
    tt.fd(10)
    tt.left(90)
    tt.fd(10)
    tt.left(-90)
    draw_t_shape()
    tt.fd(-50)
    draw_l()
    tt.fd(20)
    draw_line()
    print("Please close window with the (x) button.")
    tt.done()
    

main()
    
