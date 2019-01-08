"""
Author: Russell Harvey <rdh1896@rit.edu>
File: double_add_5.py
Assignment: Homework
Language: python3.7
Purpose: Finding values in the "double add 5" sequence using
various iterative and recursive techniques.
"""


def print_sequence_rec(start, count):
    """
    Takes a value (start) and continuously doubles it then
    adds 5 until the sequence has repeated itself (count)
    times. Done recursively, not fruitful. Prints every value
    to the console.
    Pre-Conditions: (start) and (count) should be positive to
    expect a correct outcome.
    :param start: Starting number the sequence will begin from.
    :param count: Amount of times the sequence will repeat.
    :return: empty string
    """
    if count < 0:
        pass
    else:
        print(start, end = " ")
        next_start_num = (start * 2) + 5
        print_sequence_rec(next_start_num, count - 1)
    return ""

def print_sequence_iter(start, count):
    """
     Takes a value (start) and continuously doubles it then
     adds 5 until the sequence has repeated itself (count)
     times. Done iteratively, not fruitful. Prints every value
     to the console.
     Pre-Conditions: (start) and (count) should be positive to
     expect a correct outcome.
     :param start: Starting number the sequence will begin from.
     :param count: Amount of times the sequence will repeat.
     :return: empty string
     """
    while count >= 0:
        print(start, end = " ")
        start = (start * 2) + 5
        count = count - 1
    return ""

def find_end_rec(start, count):
    """
    Takes a value (start) and continuously doubles it then
    adds 5 until the sequence has repeated itself (count)
    times. Done recursively, is fruitful. Only returns the last
    term in the sequence or itself.
    Pre-Conditions: (start) and (count) should be positive to
    expect a correct outcome.
    :param start: Starting number the sequence will begin from.
    :param count: Amount of times the sequence will repeat.
    :return: start
    """
    if count < 933:
        if count == 0:
            return start
        else:
            start = (start * 2) + 5
            return find_end_rec(start, count - 1)
    else:
        return "Recursion Error: maximum recursion depth exceeded."

def find_end_iter(start, count):
    """
    Takes a value (start) and continuously doubles it then
    adds 5 until the sequence has repeated itself (count)
    times. Done iteratively, is fruitful. Only returns the last
    term in the sequence or itself.
    Pre-Conditions: (start) and (count) should be positive to
    expect a correct outcome.
    :param start: Starting number the sequence will begin from.
    :param count: Amount of times the sequence will repeat.
    :return: start
    """
    while count >= 0:
        start = (start * 2) + 5
        count = count - 1
        if count == 0:
            return start

def find_start_rec_helper(goal, count, start):
    """
    Takes a value (goal) and then begins with a predetermined
    (start) value and attempts to count up (count) times from
    the (start) value until the (goal) has been met or surpassed.
    If goal fails to be met, the start value will increment up by 1.
    Function is created recursively and is fruitful. Only returns
    the correct start value or itself.
    Pre-Conditions: (start), (count), and (goal) should be positive to
    expect a correct outcome.
    :param start: Starting number the sequence will begin from.
    :param count: Amount of times the sequence will repeat.
    :param goal: Target number the function tries to count to.
    :return: start
    """
    value = find_end_rec(start, count)
    if value >= goal:
        return start
    else:
        return find_start_rec_helper(goal, count, start + 1)

def find_start_rec(goal, count):
    """
    Simply implements the find_start_rec_helper() function into a
    one that always starts with 0, the lowest possible start value.
    :param goal: Target number the function tries to count to.
    :param count: Amount of times the sequence will repeat.
    :return: start (from find_start_rec_helper())
    """
    return find_start_rec_helper(goal, count, 0)

def find_start_iter(goal, count):
    """
    Takes a value (goal) and then begins with the start value 0
    and attempts to count up (count) times from 0 (adding 1
    incrementally to the start variable each time it fails to meet (goal))
    until the (goal) has been met or surpassed.
    Function is created iteratively and is fruitful. Only returns
    the correct start value or itself.
    Pre-Conditions: (start), (count), and (goal) should be positive to
    expect a correct outcome.
    :param count: Amount of times the sequence will repeat.
    :param goal: Target number the function tries to count to.
    :return: start
    """
    start = 0
    value = 0
    while goal > value:
        value = find_end_iter(start, count)
        if value >= goal:
                return start
        else:
            start = start + 1

def test_cases():
    print("Sequence: Start = 5 / Count = 4 - Recursive ")
    print(print_sequence_rec(5, 4), "\n")
    print("Sequence: Start = 5 / Count = 4 - Iterative ")
    print(print_sequence_iter(5, 4), "\n")
    print("\n")
    print("Sequence: Start = 0 / Count = 10 - Recursive ")
    print(print_sequence_rec(0, 10), "\n")
    print("Sequence: Start = 0 / Count = 10 - Iterative ")
    print(print_sequence_iter(0, 10), "\n")
    print("\n")
    print("Sequence: Start = 8, Count = 6 - Recursive ")
    print(print_sequence_rec(8, 6), "\n")
    print("Sequence: Start = 8, Count = 6 - Iterative ")
    print(print_sequence_iter(8, 6), "\n")
    print("\n")
    print("Sequence: Start = 20, Count = 2 - Recursive")
    print(print_sequence_rec(20, 2), "\n")
    print("Sequence: Start = 20, Count = 2 - Iterative")
    print(print_sequence_iter(20, 2), "\n")
    print("Find End: Start = 5 / Count = 4 - Recursive ")
    print(find_end_rec(5, 4), "\n")
    print("Find End: Start = 5 / Count = 4 - Iterative ")
    print(find_end_iter(5, 4), "\n")
    print("\n")
    print("Find End: Start = 0 / Count = 10 - Recursive ")
    print(find_end_rec(0, 10), "\n")
    print("Find End: Start = 0 / Count = 10 - Iterative ")
    print(find_end_iter(0,10), "\n")
    print("\n")
    print("Find End: Start = 8, Count = 6 - Recursive ")
    print(find_end_rec(8,6), "\n")
    print("Find End: Start = 8, Count = 6 - Iterative ")
    print(find_end_iter(8, 6), "\n")
    print("\n")
    print("Find End: Start = 20, Count = 2 - Recursive")
    print(find_end_rec(20, 2), "\n")
    print("Find End: Start = 20, Count = 2 - Iterative")
    print(find_end_iter(20, 2), "\n")
    print("\n")
    print("Find Start: Start = 5 / Count = 4 - Recursive ")
    print(find_start_rec(155, 4), "\n")
    print("Find Start: Start = 5 / Count = 4 - Iterative ")
    print(find_start_iter(155, 4), "\n")
    print("\n")
    print("Find Start: Start = 0 / Count = 10 - Recursive ")
    print(find_start_rec(5115, 10), "\n")
    print("Find Start: Start = 0 / Count = 10 - Iterative ")
    print(find_start_iter(5115,10), "\n")
    print("\n")
    print("Find Start: Start = 8, Count = 6 - Recursive ")
    print(find_start_rec(827,6), "\n")
    print("Find Start: Start = 8, Count = 6 - Iterative ")
    print(find_start_iter(827, 6), "\n")
    print("\n")
    print("Find Start: Start = 20, Count = 2 - Recursive")
    print(find_start_rec(95, 2), "\n")
    print("Find Start: Start = 20, Count = 2 - Iterative")
    print(find_start_iter(95, 2), "\n")
    print("\n")

def main():
    print("The following are 4 individual test cases that I ran through each function.")
    print("The Sequence printing functions print out the correct values for each double")
    print("plus 5 sequence and helps to confirm that the find start and find end functions")
    print("work correctly.", "\n")
    test_cases()

main()