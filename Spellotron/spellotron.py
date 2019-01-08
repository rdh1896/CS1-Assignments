"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Spellotron
File: spellotron.py
Language: Python3.7
"""

import sys
from words_mode import *
from lines_mode import *


def main():
    """
    Reads input from the command line and from what is inputted, the function will use the
    argv function from sys to put the user into one of four modes:
    1. words -> User will input: "python3.7 spellotron.py words"
    2. words, done with a file -> User will input: "python3.7 spellotron.py words *file name here*"
    3. lines -> User will input: "python3.7 spellotron.py lines"
    4. lines, done with a file -> User will input: "python3.7 spellotron.py lines *file name here*"
    If any additional statements are made the function will report an error.
    :return:
    """
    if sys.argv[1] == "words":
        if len(sys.argv) == 3:
            if len(sys.argv[2]) > 5:
                if sys.argv[2][len(sys.argv) - 1] == "t":
                    words_file_read(sys.argv[2])
                else:
                    print("Error: Please input a text file.", file=sys.stderr)
            else:
                print("Error: Please input a text file.", file=sys.stderr)
        elif len(sys.argv) == 2:
            words_mode()
        else:
            print("Error: Not an accepted mode.", file=sys.stderr)
    elif sys.argv[1] == "lines":
        if len(sys.argv) == 3:
            if len(sys.argv[2]) > 5:
                if sys.argv[2][len(sys.argv) - 1] == "t":
                    lines_file_read(sys.argv[2])
                else:
                    print("Error: Please input a text file.", file=sys.stderr)
            else:
                print("Error: Please input a text file.", file=sys.stderr)
        elif len(sys.argv) == 2:
            lines_mode()
        else:
            print("Error: Not an accepted mode.", file=sys.stderr)
    else:
        print("Error: Not an accepted mode.", file=sys.stderr)


if __name__ == "__main__":
    main()
