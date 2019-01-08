"""
Tetris 2: The Sequel

Name: Russell Harvey
File: tetris2.py / Lab 02
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

def move_turtle(xpos, ypos):
    """
    Takes the parameters "xpos" and "ypos" given when called
    and moves the turtle to the target location. Can be called
    to move the turtle to and from the datum point by re-calling
    the function and changing the sign of xpos and ypos to be negative.
    Pre-Condition: Turtle is up, facing east. Located at the datum point
    or at a given coordinate on the board.
    Post-Condition: Turtle is up, facing east. Located at the datum point
    or a given coordinate on the board.
    """
    if xpos > 9 or ypos > 19:
        print("Error: Location not on board.")
    else:
        tt.fd(xpos * 10)
        tt.left(90)
        tt.fd(ypos * 10)
        tt.right(90)

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

def draw_t_shape(rot):
    """
    Draws the "upside down 'T'" Tetris shape on the canvas.
    Rotated to a given position.
    Pre-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "T shape".
    Post-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "T shape".
    """
    tt.fillcolor("blue")
    if rot == 0:
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
    elif rot == 90:
        tt.fd(10)
        tt.left(90)
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
        tt.right(90)
        tt.fd(-10)
    elif rot == 180:
        tt.left(90)
        tt.fd(20)
        tt.right(90)
        tt.fd(20)
        tt.left(180)
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
        tt.fd(20)
        tt.left(90)
        tt.fd(20)
        tt.left(90)
    elif rot == 270:
        tt.right(90)
        tt.fd(-30)
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
        tt.fd(30)
        tt.left(90)
    else:
        print("Error: rotational angle not supported.")

def draw_square(rot):
    """
    Draws the "sqaure" shaped Tetris block on the canvas.
    Pre-Conditions: Turtle is up, facing east, located on the
    bottom left corner of the "square" shape.
    Post-Conditions: Turtle is up, facing east, located on the
    bottom left corner of the "square" shape.
    """
    tt.fillcolor("red")
    if rot == 0 or rot == 90 or rot == 180 or rot == 270:
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(10)
        tt.left(90)
        tt.fd(10)
        draw_block()
        tt.fd(10)
        tt.left(90)
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(20)
        tt.left(-90)
        tt.fd(10)
        tt.left(180)
    else:
        print("Error: Rotational angle not supported.")

def draw_l_shape(rot):
    """
    Draws the "L" shaped Tetris block. Rotated to a given position.
    Pre-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "L" shape.
    Post-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "L" shape.
    """
    tt.fillcolor("orange")
    if rot == 0:
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-10)
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
    elif rot == 90:
        tt.fd(30)
        tt.left(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-10)
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.right(90)
        tt.fd(-30)
    elif rot == 180:
        tt.fd(10)
        tt.left(90)
        tt.fd(30)
        tt.left(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-10)
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.right(90)
        tt.fd(-30)
        tt.right(90)
        tt.fd(-10)
    elif rot == 270:
        tt.left(90)
        tt.fd(20)
        tt.right(180)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-10)
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.left(180)
        tt.fd(-20)
        tt.right(90)
    else:
        print("Error: Rotational angle not supported.")

def draw_line(rot):
    """
    Draws the "line" shaped Tetris block. Rotated to a given position.
    Pre-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "line" shape.
    Post-Conditions: Turtle is up, facing east, located in the
    bottom left corner of the "line" shape.
    """
    tt.fillcolor("green")
    if rot == 0 or rot == 180:
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
    elif rot == 90 or rot == 270:
        tt.right(90)
        tt.fd(-10)
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
        tt.fd(10)
        tt.left(90)
    else:
        print("Error: Rotational value not supported.")

def draw_s_shape(rot):
    """
    Draws the S shaped Tetris block. Rotated to a given position.
    Pre-Conditions: Turtle is up, facing east. Located at the bottom
    left corner of the shape.
    Post-Conditions: Turtle is up, facing east. Located at the bottom
    left corner of the shape.
    """
    tt.fillcolor("yellow")
    if rot == 0 or rot == 180:
        draw_block()
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-20)
        tt.right(90)
        tt.fd(10)
        tt.left(90)
    elif rot == 90 or rot == 270:
        tt.fd(10)
        tt.left(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-20)
        tt.right(90)
        tt.fd(10)
        tt.left(90)
        tt.right(90)
        tt.fd(-10)
    else:
        print("Error: Rotational angle not supported.")

def draw_z_shape(rot):
    """
    Draws the "Z" shaped Tetris block. Rotated to a given position.
    Pre-Conditions: Turtle is up, facing east. Located at the bottom
    left corner of the shape.
    Post-Conditions: Turtle is up, facing east. Located at the bottom
    left corner of the shape.
    """
    tt.fillcolor("purple")
    if rot == 0 or rot == 180:
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-10)
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.fd(-10)
        draw_block()
        tt.fd(10)
        tt.right(90)
        tt.fd(10)
        tt.left(90)
    elif rot == 90 or rot == 270:
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.fd(-10)
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.fd(-10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.left(180)
    else:
        print("Error: Rotational angle not supported.")


def draw_j_shape(rot):
    """
    Draws the "J" shaped Tetris block. Rotated to a given value.
    Pre-Conditions: Turtle is up, facing east. Located at the bottom
    left corner of the shape.
    Post-Conditions: Turtle is up, facing east. Located at the bottom
    left corner of the shape.
    """
    tt.fillcolor("coral")
    if rot == 0:
        draw_block()
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.fd(-10)
    elif rot == 90:
        tt.fd(10)
        tt.left(90)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.fd(-10)
        tt.right(90)
        tt.fd(-10)
    elif rot == 180:
        tt.left(90)
        tt.fd(30)
        tt.right(90)
        tt.fd(20)
        tt.left(180)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.fd(-10)
        tt.fd(20)
        tt.left(90)
        tt.fd(30)
        tt.left(90)
    elif rot == 270:
        tt.left(90)
        tt.fd(20)
        tt.left(180)
        draw_block()
        tt.fd(10)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.left(90)
        tt.fd(10)
        tt.right(90)
        draw_block()
        tt.right(90)
        tt.fd(20)
        tt.left(90)
        tt.fd(-10)
        tt.fd(20)
        tt.left(90)
    else:
        print("Error: Rotational angle not supported.")




def draw_shape(xpos, ypos, rot, shape):
    """
    Moves turtle from the datum point to a target
    location then draws a shape. After completion
    of the shape, the turtle returns to the datum point.
    Pre-Condition: Turtle is up, facing east. Located at
    the datum point.
    Post-Condition: Turtle is up, facing east. Located at
    the datum point.
    """
    move_turtle(xpos, ypos)
    if shape == "B":
        draw_square(rot)
    elif shape == "I":
        draw_line(rot)
    elif shape == "L":
        draw_l_shape(rot)
    elif shape == "J":
        draw_j_shape(rot)
    elif shape == "Z":
        draw_z_shape(rot)
    elif shape == "S":
        draw_s_shape(rot)
    elif shape == "T":
        draw_t_shape(rot)
    else:
        print("Error: Not a valid shape.")
    move_turtle(-1 * xpos, -1 * ypos)

def ask_user():
    """
    Gets the user to input values for the row number,
    column number, shape, and rotational value. Then
    plugs those in to the draw_shape function and draws
    a shape based on the given parameters.
    """
    given_y_coord = input("Enter row number: ")
    given_x_coord = input("Enter column number: ")
    given_shape = input("Choose Shape: ")
    given_rot = input("Rotation value?: ")
    draw_shape(int(given_x_coord), int(given_y_coord), int(given_rot), str(given_shape))

def main():
    """
    Initializes the turtle, then draws the board. After that,
    the 7 Tetris shapes are drawn on the board in various
    arrangements all in legal Tetris form. The function then prompts
    the user to enter in a row, column, shape, and rotation to
    place another Tetris shape on the board according to their parameters.
    After this the program will terminate upon the user closing the window.
    Pre-Conditions: Turtle is down, facing east.
    Post-Conditions: Turtle is up, facing east. Located at the datum point.
    """
    initialize()
    draw_board()
    draw_shape(1, 0, 270, "J")
    draw_shape(4, 0, 0, "B")
    draw_shape(6, 0, 90, "Z")
    draw_shape(9, 0, 180, "L")
    draw_shape(2, 1, 0, "S")
    draw_shape(4, 3, 90, "I")
    draw_shape(8, 3, 180, "T")
    ask_user()
    print("Please press (x) to close the program.")
    tt.done()

main()