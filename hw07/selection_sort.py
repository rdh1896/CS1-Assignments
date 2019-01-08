"""
Name: Russell Harvey <rdh1896@rit.edu>
File: selection_sort.py
Assignment: hw07
Language: Python 3.7

Questions:
1. If the list is already ordered properly the insertion sort will perform better than a selection sort. This is
because the insertion sort only needs to go through each value of the list once in order to determine that it is sorted
making the time complexity O(n) and very easy for the computer to handle.
2. The selection sort would have a tougher time sorting the list as fast as an insertion sort would with an already
sorted list of values because the values in the list are iterated over more than once because every time the function
makes a swap a segment of the list must be iterated over again to find a new minimum. The time complexity of selection
sort is always O(n(n-1)/2) where as insertion sort varies from O(n) to O(n^2).
"""

def create_list():
    """
    Takes a user input for a file then opens it and reads every
    line and puts the number value from every line into a list and
    returns the list.
    Pre-Conditions: File is formatted where there is one integer on every
    line of the text file.
    :return: lst
    """
    file = input("Please enter file name: ")
    sequence = open(file)
    lst = []
    line = sequence.readline()
    while True:
        if line == "":
            break
        else:
            line.strip()
            line = int(line)
            lst.append(line)
            line = sequence.readline()
    return lst

def find_min_from(lst, n):
    """
    Finds the minimum value within a specified range of a list and then
    returns that value.
    :param lst: List the function is looking through.
    :param n: Specified range of the list the function will search through.
    :return: current_min
    """
    current_min = lst[n]
    for i in lst[n:]:
        if current_min > i:
            current_min = i
        else:
            pass
    return current_min

def swap(lst, current, min):
    """
    Swaps two values in a list. For the sake of this program, it will switch
    the minimum value with the current one if the current is greater than the minimum.
    :param lst: List the swapping occurs in.
    :param current: Current value the "pointer" is on.
    :param min: Minimum value within the specified range.
    :return: lst
    """
    a = lst.index(current)
    b = lst.index(min)
    lst[a], lst[b] = lst[b], lst[a]
    return lst

def selection_sort(lst):
    """
    Takes a list as a parameter and then sorts it numerically ascending
    using the selection sort algorithm.
    Pre-Conditions: List must only contain integers.
    :param lst: List which is being sorted.
    :return: lst
    """
    for i in range(len(lst) - 1):
        min = find_min_from(lst, i)
        if min < lst[i]:
            lst = swap(lst, lst[i], min)
        else:
            pass
    return lst

def main():
    """
    Creates a list from a text doctument then prints it. After, it will
    sort the list using a selection sort algorithm and then print the sorted
    list to the console.
    :return: None
    """
    lst = create_list()
    print("Original List: ", lst)
    print("Sorted List: ", selection_sort(lst))

main()


