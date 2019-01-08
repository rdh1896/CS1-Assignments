"""
File: HW08.py
Author: Russell Harvey <rdh1896@rit.edu>
"""

import random
import time
import merge_sort
import insertion_sort
import quick_sort


def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.randint(1,100)]
    return L


def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()*i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8)*i]
    return L

def merge_quick_sort(lst):
    """
    Takes an unsorted list, splits it in half, applies quick_sort
    on both halves, then merges both halves back together. This will
    result in a perfectly sorted list.
    Pre-Conditions: "lst" should be unsorted
    Post-Conditions: The original "lst" should be sorted
    :param lst: A inputted unsorted list
    :return: merge_sort.merge(sorted_lst1, sorted_lst2)
    """
    lst1, lst2 = merge_sort.split(lst)
    sorted_lst1 = quick_sort.quick_sort(lst1)
    sorted_lst2 = quick_sort.quick_sort(lst2)
    return merge_sort.merge(sorted_lst1, sorted_lst2)

def merge_quick_sort_test():
    """
    Tests the merge_quick_sort function using a list of 20 random
    characters. Prints the original list then the list after being sorted.
    :return: None
    """
    lst = get_list2(20)
    print("Testing the correctness of merge_quick_sort:")
    print("Before Sorted:")
    print(lst)
    sorted_list = merge_quick_sort(lst)
    print("After Sorted:")
    print(sorted_list)
    print("\n")

def test_compare():
    """
    Takes 4 different random lists with 10,000 terms in each and runs them
    through each sorting method (insertion, merge, merge_quick, and quick).
    When doing this, the function times how long it takes for each method to
    process each list. The function prints the trials for each list into sectioned
    blocks showing the results for each list for every sorting method.
    :return: None
    """
    print("Time comparison test begins.")
    print("All lists used in this test are of length 10000.")
    print("\n")
    n = 10000
    list_num = 1
    test_lists = [get_list1(n), get_list2(n), get_list3(n), get_list4(n)]
    for i in test_lists:
        if list_num == 1:
            print("Testing with list 1 - random elements")
        elif list_num == 2:
            print("Testing with list 2 - repeated elements")
        elif list_num == 3:
            print("Testing with list 3 - overall increasing elements, not favorable to quick sort")
        elif list_num == 4:
            print("Testing with list 4 - not favorable to quick sort")
        insertion_lst = i[:]
        start = time.time()
        insertion_sort.insertion_sort(insertion_lst)
        end = time.time()
        print("selection_sort Elapsed Time: ", end - start, "seconds")
        merge_lst = i[:]
        start = time.time()
        merge_sort.merge_sort(merge_lst)
        end = time.time()
        print("merge_sort Elapsed Time: ", end - start, "seconds")
        merge_quick_lst = i[:]
        start = time.time()
        merge_quick_sort(merge_quick_lst)
        end = time.time()
        print("merge_quick_sort Elapsed Time: ", end - start, "seconds")
        quick_lst = i[:]
        start = time.time()
        quick_sort.quick_sort(quick_lst)
        end = time.time()
        print("quick_sort Elapsed Time: ", end - start, "seconds")
        print("\n")
        list_num += 1

def main():
    """
    Simply composes the merge_quick_sort_test() and test_compare() functions
    into one function and executes each.
    :return: Nonev
    """
    merge_quick_sort_test()
    test_compare()

main()

