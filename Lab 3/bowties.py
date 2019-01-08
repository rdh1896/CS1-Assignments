"""
Author: Russell Harvey <rdh1896@rit.edu>
File: bowties.py
Assignment: lab03
Language: Python
"""

import turtle as tt

def initialize():
    """
    Initializes the turtle and sets the canvas
    size to 600 x 600 units.
    Pre-Conditions: Turtle is down, facing east.
    Post-Conditions: Turtle is up, facing east. Located at
    the center of the largest bow tie.
    :return: 0
    """
    tt.setup(600, 600)
    tt.up()

def draw_bowtie(size):
    """
    Draws one bow tie shape on the canvas.
    Pre-Conditions: Turtle is up, facing east. Located at
    the center of the bow tie about to be drawn. Pen color black.
    Post-Conditions: Turtle is up, facing east. Located at
    the center of the bow tie just drawn. Pen color black, fill color orange.
    :param size: Accepts any number value for the size of the bow tie.
    :return: 0
    """
    tt.down()
    tt.left(30)
    tt.fd(size)
    tt.right(120)
    tt.fd(size)
    tt.right(120)
    tt.fd(2 * size)
    tt.left(120)
    tt.fd(size)
    tt.left(120)
    tt.fd(size)
    tt.right(30)
    tt.up()
    tt.fillcolor("orange")
    tt.right(90)
    tt.fd(size/4)
    tt.left(90)
    tt.down()
    tt.begin_fill()
    tt.circle(size/4)
    tt.end_fill()
    tt.up()
    tt.left(90)
    tt.fd(size/4)
    tt.right(90)

def draw_bowties(size, depth):
    """
    Takes the parameters size (size of the bow tie) and depth (recursive depth
    of the function) and draws multiple bow ties recursively.
    Pre-Conditions: Turtle is up, facing east. Located at
    the center of the largest bow tie.
    Post-Conditions: Turtle is up, facing east. Located at
    the center of the largest bow tie.
    :param size: Size of the largest drawn bow tie.
    :param depth: Depth of the recursive function.
    :return: 0
    """
    if depth <= 0:
        pass
    else:
        draw_bowtie(size)
        tt.left(30)
        tt.fd(2 * size)
        draw_bowties(size / 3, depth - 1)
        tt.fd(-2 * size)
        tt.left(120)
        tt.fd(2 * size)
        tt.left(180)
        draw_bowties(size / 3, depth - 1)
        tt.fd(2 * size)
        tt.left(30)
        tt.right(30)
        tt.fd(2 * size)
        draw_bowties(size / 3, depth - 1)
        tt.fd(-2 * size)
        tt.right(120)
        tt.fd(2 * size)
        tt.right(180)
        draw_bowties(size / 3, depth - 1)
        tt.fd(2 * size)
        tt.right(30)

def main():
    """
    Initallizes the turtle, then asks the user to define
    a depth for the draw_bowties() function, then draws
    bowties recursively to the deisred depth.
    Pre-Conditions: Turtle is down, facing east.
    Post-Conditions: Turtle is up, facing east. Located
    at the center of the largest bow tie.
    :return:
    """
    initialize()
    depth = input("Please enter the depth of recursion: ")
    depth = int(depth)
    draw_bowties(100, depth)
    tt.done
    print("Please press (x) to close the program")

main()
