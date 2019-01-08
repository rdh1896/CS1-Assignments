"""
Name: Russell "Kevin" Harvey
Assignment: Lab 09
File: ball_puzzle.py
Language: Python
"""

import stack
import ball_puzzle_animate as animate

def main():
    """
    Creates 3 cans, one for each color, and stores them in a list.
    Then asks the user to input a string of characters containing the
    letters "R", "G", and "B" corresponding to the different ball colors.
    Calls the animate_init function to setup the balls in the animation then
    places each ball in a stack formed by a dataclass structure. After this it uses
    my solve_puzzle function to solve the puzzle and displays the amount of moves it
    takes to sort the balls. Asks the user to close the window and calls the animate_finish
    function to stop the animation.
    :return: None
    """
    red_can = stack.make_empty_stack()
    blue_can = stack.make_empty_stack()
    green_can = stack.make_empty_stack()
    cans = [red_can, green_can, blue_can]
    balls = input("Please input your desired balls: ")
    animate.animate_init(balls)
    for ch in balls:
        stack.push(red_can, ch)
    print("Moves required: ", solve_puzzle(red_can, green_can, blue_can))
    print("Close the window to quit.")
    animate.animate_finish()

def solve_puzzle(red, green, blue):
    """
    Takes in three stacks and then sorts them based on ball color.
    First it checks each ball in the red can. If the ball is green it
    goes in green, if the ball is red or blue it goes in blue. Then it
    looks at the blue can. If the ball is red it goes in the red, if it
    is blue it goes in the green. Lastly all the blue balls in the green
    can move back to the blue can and the stacks of balls will be sorted.
    The function also tracks the amount of moves the sorting process takes
    and returns it.
    Pre-Conditions: It is assumed that all balls will begin in the red can and
    that the green and blue cans are empty.
    :param red: Red Can
    :param green: Green Can
    :param blue: Blue Can
    :return: moves
    """
    moves = 0
    stack_list = [red, green, blue]
    while stack.is_empty(red) != True:
        top_val = stack.top(red)
        if top_val == "R" or top_val == "B":
            stack.pop(red)
            stack.push(blue, top_val)
            animate.animate_move(stack_list, 0, 2)
        else:
            stack.pop(red)
            stack.push(green, top_val)
            animate.animate_move(stack_list, 0, 1)
        moves += 1
    while stack.is_empty(blue) != True:
        top_val = stack.top(blue)
        if top_val == "R":
            stack.pop(blue)
            stack.push(red, top_val)
            animate.animate_move(stack_list, 2, 0)
        else:
            stack.pop(blue)
            stack.push(green, top_val)
            animate.animate_move(stack_list, 2, 1)
        moves += 1
    while stack.top(green) != "G":
        top_val = stack.top(green)
        stack.pop(green)
        stack.push(blue, top_val)
        animate.animate_move(stack_list, 1, 2)
        moves += 1
    return moves

main()
