"""
This program includes a function to test
whether a given codeword string is a valid encoding
of a given original string using a Caesar cipher.

It returns an integer value, indicating the
forward shift (e.g A (original) -> B (codeword)
is a forward shift of 1).

It is assumed that the original string and codeword string
both comprise only capitalized English letters A-Z.

It is also assumed that neither the original string
nor the codeword string is the empty string.

A valid encoding results in a return value
in the range 0-25, indicating the forward shift
value used in the cipher.
A return value of 0 indicates a valid Caesar cipher
that used no shift at all.

A -1 is returned to indicate that the given
codeword string is not a valid encoding of the original
string using a Caesar cipher.

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

File:  test_debug1.py
Author: CS @ RIT
Author: (add your name here)

"""


def caesar(original, codeword):
    """
    Tests whether the provided codeword string
    represents a valid encoding of the original
    string using a Caesar cipher.
    Pre-condition:  both the codeword and original
    are strings containing only capitalized English
    letters.
    Pre-condition:  neither the codeword nor the
    original string is the empty string.
    :param original: The original string.
    :param codeword: The encoded string.
    :return: Integer in the range 0-25 if the codeword
    represents a valid encoding of the original
    string using a Caesar cipher.
    Returns -1 otherwise.
    """

    # Use built-in ord() function to get ASCII
    # integer value associated with A-Z.
    # A has value 65, B is 66, ..., Z is 90.

    # Get shift for first character.  All characters must
    # have identical shift for it to be a valid Caesar shift.
    if ord(codeword[0]) >= ord(original[0]):
        shift = ord(codeword[0]) - ord(original[0])
    else:
        shift = 26 - (ord(original[0]) - ord(codeword[0]))

    for idx in range(len(codeword)):
        if ord(original[idx]) < ord(codeword[idx]):
            if ord(codeword[idx]) - ord(original[idx]) != shift:
                return -1
        elif ord(original[idx]) > ord(codeword[idx]):
            if (26 - (ord(original[idx]) - ord(codeword[idx]))) != shift:
                return -1

    return shift

def test_suite():
    """
    All expected caesar values are forward shifts.
    """
    print("Expected Caesar: 0 | Actual Caesar: ", caesar("very", "very"))
    print("Expected Caesar: 1 | Actual Caesar: ", caesar("very", "wfsz"))
    print("Expected Caesar: 2 | Actual Caesar: ", caesar("very", "xgta"))
    print("Expected Caesar: 3 | Actual Caesar: ", caesar("very", "yhub"))
    print("Expected Caesar: 4 | Actual Caesar: ", caesar("very", "zivc"))
    print("Expected Caesar: 5 | Actual Caesar: ", caesar("very", "ajwd"))
    print("Expected Caesar: 6 | Actual Caesar: ", caesar("very", "bkxe"))
    print("Expected Caesar: 7 | Actual Caesar: ", caesar("very", "clyf"))
    print("Expected Caesar: 8 | Actual Caesar: ", caesar("very", "dmzg"))
    print("Expected Caesar: 9 | Actual Caesar: ", caesar("very", "enah"))
    print("Expected Caesar: 10 | Actual Caesar: ", caesar("very", "fobi"))
    print("Expected Caesar: 11 | Actual Caesar: ", caesar("very", "gpcj"))
    print("Expected Caesar: 12 | Actual Caesar: ", caesar("very", "hqdk"))
    print("Expected Caesar: 13 | Actual Caesar: ", caesar("very", "irel"))
    print("Expected Caesar: 14 | Actual Caesar: ", caesar("very", "jsfm"))
    print("Expected Caesar: 15 | Actual Caesar: ", caesar("very", "ktgn"))
    print("Expected Caesar: 16 | Actual Caesar: ", caesar("very", "luho"))
    print("Expected Caesar: 17 | Actual Caesar: ", caesar("very", "mvip"))
    print("Expected Caesar: 18 | Actual Caesar: ", caesar("very", "nwjq"))
    print("Expected Caesar: 19 | Actual Caesar: ", caesar("very", "oxkr"))
    print("Expected Caesar: 20 | Actual Caesar: ", caesar("very", "pyls"))
    print("Expected Caesar: 21 | Actual Caesar: ", caesar("very", "qzmt"))
    print("Expected Caesar: 22 | Actual Caesar: ", caesar("very", "ranu"))
    print("Expected Caesar: 23 | Actual Caesar: ", caesar("very", "sbov"))
    print("Expected Caesar: 24 | Actual Caesar: ", caesar("very", "tcpw"))
    print("Expected Caesar: 25 | Actual Caesar: ", caesar("very", "udqx"))

test_suite()


