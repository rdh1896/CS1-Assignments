"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Lab 06
File: select_median.py
Language: Python 3.7
"""

import time


def quick_select(lst, k):
    """
    Takes in a list and then finds the "kth smallest value" in the list.
    Uses a method similar to a quick sort algorithm to locate a number as
    if the list was already sorted.
    Pre-conditions: "lst" should be unsorted
    :param lst: List of terms passing through quick_select()
    :param k: Defines the location of the term we are searching for in the unsorted
    list. "kth smallest value" will essentially return the value at index "k - 1" if the
    list was sorted.
    :return: pivot, quick_select(smaller_lst, k), quick_select(larger_lst, k - m - count)
    """
    pivot = lst[len(lst) // 2]
    smaller_lst = []
    larger_lst = []
    count = 0
    for element in lst:
        if element < pivot:
            smaller_lst.append(element)
        elif element > pivot:
            larger_lst.append(element)
        else:
            count += 1
    m = len(smaller_lst)
    if m <= k < m + count:
        return pivot
    elif m > k:
        return quick_select(smaller_lst, k)
    else:
        return quick_select(larger_lst, k - m - count)


def find_sum(lst, best):
    """
    Finds the sum of the distances between a "best" point and all other terms
    in a list.
    Pre-conditions: "best" must be a term in "lst".
    :param lst: List of terms, including "best", that pass through the function.
    :param best: The number which we will calculate the distance from that point to
    all others in the list.
    :return: sum
    """
    sum = 0
    for element in range(len(lst) - 1):
        sum = sum + abs(best - lst[element])
    return sum


def main():
    """
    Asks the user to input a file, then reads each line. The function will split the lines at
    a space in the file and then will append a number to "lst". This creates a list of numbers
    from the inputted text file. Then, if the number of terms in the list is even the function
    runs quick_select() twice. Once with "k" being the "middle" of the list, and once with "k" being
    one term behind that. Then those two outputs will be added and divided by two to produce the median
    of the list. If list is odd, quick_select() only needs to run once with "k" being the middle of the
    list. This will get the median of the list as well. After each quick_select() run, the median
    (or "best" as I named it) value will be plugged into the find_sum() function along with the list
    and will get the distance between the median and all other points. Time is also calculated from the time
    the file gets read, to the time quick select has finished its processes. The function will display the optimum
    store location (median), sum of distances to new store, and the elapsed time for the process to run.
    Pre-condition: "lst" should be unsorted.
    :return: None
    """
    lst = []
    file = open(input("Please enter file name: "))
    line = file.readline()
    while True:
        if line == "":
            break
        else:
            line = line.strip()
            split_line = line.split(" ")
            value = int(split_line[1])
            lst.append(value)
            line = file.readline()
    if len(lst) % 2 == 0:
        start = time.time()
        q1 = quick_select(lst, len(lst) // 2)
        q2 = quick_select(lst, len(lst) // 2 - 1)
        best_location = (q1 + q2) / 2
        end = time.time()
        sum_distances = find_sum(lst, best_location)
        time_elapsed = end - start
    else:
        start = time.time()
        best_location = quick_select(lst, len(lst) // 2)
        end = time.time()
        sum_distances = find_sum(lst, best_location)
        time_elapsed = end - start
    print("Optimum new store location: ", best_location)
    print("Sum of distances to new store: ", sum_distances, "\n")
    print("elapsed time", time_elapsed)


if __name__ == "__main__":
    main()
