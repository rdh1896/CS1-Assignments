"""
Author: Russell Harvey
File: hw01
"""
import turtle as tt

def startup():
    """
    Sets the turtle at the bottom left corner of the north-most triangle so that the star is centered on the canvas.
    The turtle will be facing east ready to draw the top triangle in the five point star.
    Pre-Condition: Turtle will be in the center of the canvas, pen is up, and facing east.
    Post-Condition: Turtle will be pen up, facing east, located in the bottom left of the north triangle.
    """
    tt.up()
    tt.left(90 + 54) #Turns the turtle so that it is facing the bottom left corner of the north triangle
    tt.fd(55.9017) #Moves the turtle to the start location
    tt.right(90 + 54)

def draw_star():
    """
    Tells the turtle to draw a 5 point star
    Pre-Condition:  Turtle will be pen up, facing east, located in the bottom left of the north triangle.
    Post-Condition:  Turtle will be pen up, facing east, located in the bottom left of the north triangle.
    """
    draw_triangle()
    draw_triangle()
    draw_triangle()
    draw_triangle()
    draw_triangle()

def draw_triangle():
    """
    Creates one equilateral triangle with dimensions of 50 units per side and
    then rearranges the position of the turtle to draw the next triangle (right of
    the triangle just drawn) in the five point star pattern.
    Pre-Condition: Turtle will always be located in the bottom left corner of the triangle that will be drawn,
    facing the direction necessary to draw the base of the triangle with respect to the star's shape, pen is up.
    Post-Condition: Turtle will be located in the bottom right corner of the triangle just drawn, will be pointed
    in the direction of the next triangle's base with respect to the star, pen is up.
    """
    tt.down()
    draw_side()
    draw_side()
    draw_side()
    tt.up()
    tt.fd(50)
    tt.right(72)

def draw_side():
    tt.fd(50)
    tt.left(120)

def main():
    """
    Main function of the program. Creates a canvas, then moves the turtle to a starting position.
    The program then creates 5 small triangles that arrange themselves to form a five point star.
    After the program is complete, instructions are printed for the user to close the program.
    Pre-Condition: Turtle is centered on the canvas, pen down, facing east.
    Post-Condition: Turtle will be pen up, facing east, located in the bottom left of the north triangle.
    """
    startup()
    draw_star()
    # I put 'hideturtle' in the function so the turtle eliminates itself from the canvas after creation of the star
    tt.hideturtle()
    print("Please press the (x) button to close the program")
    tt.done()
    print("Ciao.")

main()

