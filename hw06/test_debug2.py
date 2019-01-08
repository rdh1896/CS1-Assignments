"""
This program includes a function to find and return
the length of a longest common consecutive substring
shared by two strings.

If the strings have nothing in common, the longest
common consecutive substring has length 0.

For example, if string1 = "established", and
string2 = "ballistic", the function returns the
integer 3, as the string "lis" is the longest common
consecutive substring shared by the two strings.

The function tests all possible pairs of starting points
(starting point for string 1, and starting point for string 2),
and measures the match from each.  It keeps
track of the length of the best match seen,
and returns that when finished checking all starting points.

The function has bug(s).

There are no tests (yet).

Your job is to
1) include in this program a sufficient
suite of pass/fail tests to thoroughly
test the function and expose all error(s).

2) Generate a screenshot that
demonstrates your use of a debugger
to step through the function. Specifically it should
illustrate the execution point of a test at
which the function makes (or is about to make)
a mistake.

3) fix the code and document your fix(es).
Include additional tests if you feel it
necessary to thoroughly test the function.

You will submit your updated version of this
file (along with a separate document containing
the screenshot and answered questions).

File:  test_debug2.py
Author: Russell Harvey <rdh1896@rit.edu>

"""


def match(string1, string2):
    """
    Identifies and returns the length of a longest
    common consecutive substring shared
    by the two input strings.
    :param string1: The first string.
    :param string2: The second string.
    :return: length of a longest shared consecutive string.
    """

    best_length = 0
    max_length1 = len(string1) - 1
    max_length2 = len(string2) - 1
    # for all possible string1 start points
    for idx1 in range(max_length1):
        # for all possible string2 start points
        for idx2 in range(max_length2):
            # check if these characters match
            if string1[idx1] == string2[idx2]:
                this_match_count = 1
                # see how long the match continues
                while idx1 + this_match_count <= max_length1 and idx2 + this_match_count <= max_length2:
                    current_index1 = idx1 + this_match_count
                    current_index2 = idx2 + this_match_count
                    if string1[current_index1] == string2[current_index2]:
                        this_match_count += 1
                    else:
                        break

                # compare to best so far
                if this_match_count > best_length:
                    best_length = this_match_count

    # now return the result
    return best_length

def test_cases():
    print("Expected Output: 3 |", " Actual Output: ", match("APPle", "APPLe"))
    print("Expected Output: 2 |", " Actual Output: ", match("ApPLe", "APPLE"))
    print("Expected Output: 3 |", " Actual Output: ", match("aPPLE", "apPLEs"))
    print("Expected Output: 3 |", " Actual Output: ", match("established", "ballistic"))
    print("Expected Output: 3 |", " Actual Output: ", match("ballistic", "established"))
    print("Expected Output: 2 |", " Actual Output: ", match("98242435451241234", "58594762398745623"))
    print("Expected Output: 5 |", " Actual Output: ", match("978321649812814092841431214", "2139486897234619284187401"))
    print("Expected Output: 5 |", " Actual Output: ", match("fished", "established"))
    print("Expected Output: 5 |", " Actual Output: ", match("established", "fished"))

test_cases()