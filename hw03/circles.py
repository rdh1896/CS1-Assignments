"""
File: circles.py
Assignment: homework
Language: python3.7
Author: Russell Harvey <rdh1896@rit.edu>
Purpose: Draws a circle pattern that reiterates itself a
given set of times.
"""

import turtle as tt

def draw_circles(radius, depth):
    """
    The function recursively draws circles at the
    left and rightmost points of previously drawn
    circles.
    :param radius: The radius of the current circle
    :param depth: The active depth of the recursive function
    Pre-Conditions: 'depth' and 'radius' are both greater than
    or equal to zero, turtle is facing east, pen is down.
    Post-Conditions: Circles were drawn for the current depth,
    turtle is facing east, pen is up.
    """
    if depth == 1:
        tt.circle(radius)
    elif depth > 1:
        tt.circle(radius)
        tt.up()
        tt.left(90)
        tt.fd(radius)
        tt.right(90)
        tt.fd(radius)
        tt.down()
        draw_circles(radius / 2, depth - 1)
        tt.up()
        tt.left(180)
        tt.fd(radius * 2)
        tt.left(180)
        tt.down()
        draw_circles(radius / 2, depth - 1)
        tt.up()
        tt.fd(radius)
        tt.right(90)
        tt.fd(radius)
        tt.left(90)

def main():
    """
    Prompts the user to input an 'N' value which is then
    inputted into the draw_circles function defining the
    depth of the recursive function. The draw_circles function
    is then executed to the given depth.
    Pre-Conditions: Turtle is down, facing east.
    Post-Conditions: Cicles have been drawn to the given depth,
    turtle is facing east located at the bottom of the largest
    circle, pen is up.
    """
    n = input("Please input an 'N' value (depth of the function): ")
    n = int(n)
    draw_circles(100, n)
    print("Press (x) to end the program")

main()