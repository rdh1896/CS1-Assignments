"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Lab 06
File: store_location.py
Language: Python 3.7
"""

import time


def partition(pivot, lst):
    """
    Takes in a list, and partitions it based on a pivot. Items less than the pivot
    will be put in the list "less", items more than the pivot will be put in the list
    "more", and items equal to the pivot will be put in the list "same".
    Pre-conditions: "lst" should be unsorted and only contain "int" types
    :param pivot: Value which the list will be partitioned about
    :param lst: List passing through the function
    :return: (less, same, more)
    """
    (less, same, more) = ([], [], [])
    for element in lst:
        if element > pivot:
            more.append(element)
        elif element < pivot:
            less.append(element)
        else:
            same.append(element)
    return (less, same, more)


def quick_sort(lst):
    """
    Takes in a list and uses the quick sort method of sorting to sort a list of
    integers from smallest to largest. When the list is fully sorted, the function
    will return the sorted list.
    Pre-conditions: List should be unsorted and only contain "int" types.
    :param lst: List being passed through the function
    :return: lst, quick_sort(less) + same + quick_sort(more)
    """
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        (less, same, more) = partition(pivot, lst)
        return quick_sort(less) + same + quick_sort(more)


def find_median(lst):
    """
    Finds the median value in a list. Has adjustments to calculate the median
    if there is a even amount of values or an odd amount of values. It will
    quick sort the list at the beginning to make sure it is sorted.
    Pre-conditions: "lst" should be unsorted and only contain "int" types
    :param lst: List being passed through the function.
    :return: (sorted_list[len(lst) // 2] + sorted_list[len(lst) // 2 - 1]) / 2,
    sorted_list[len(lst) // 2]
    """
    sorted_list = quick_sort(lst)
    if len(lst) % 2 == 0:
        return (sorted_list[len(lst) // 2] + sorted_list[len(lst) // 2 - 1]) / 2
    else:
        return sorted_list[len(lst) // 2]


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
    Asks user to input a file, then reads every line of the file splitting off the initial string
    in the file and then taking the number after that, converting it into a integer then placing
    it in a list. After that, the function begins a timer then then finds the median of the list
    and then ends the timer. The distance of every point to the median is then summed up and placed
    in a variable. The function prints the median, sum, and time elapsed.
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
    start = time.time()
    best_location = find_median(lst)
    end = time.time()
    sum_distances = find_sum(lst, best_location)
    time_elapsed = end - start
    print("Optimum new store location: ", best_location)
    print("Sum of distances to new store: ", sum_distances, "\n")
    print("elapsed time", time_elapsed)


if __name__ == "__main__":
    main()
