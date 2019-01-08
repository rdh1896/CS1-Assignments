"""
file: test_link_sort.py
author: Russell Harvey <rdh1896@rit.edu>
description: tester for functions in linked_insort.py
"""

import linked_insort
import linked_code
from dataclasses import dataclass
from typing import Any, Union

@dataclass(frozen=True)
class LinkNode:
    """
        Creates a linked structure dataclass when called. Because it is frozen,
        the class is immutable. Has variables "value" which can be any type and
        rest which is a union of None and the class itself.
    """
    value : Any
    rest : Union[None, "Node"]

def read_file( fname ):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
    """
    file = open(fname)
    lst = []
    for line in file:
        line = line.strip()
        line = int(line)
        lst.append(line)
    return linked_code.mk_linked_list_rec(lst)

def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )
    original_s = read_file(name)
    if original_s is None:
        print("Please enter a file that contains data.")
        return main()
    else:
        print( "unsorted:", original_s )

        sorted_s = linked_insort.insort( original_s )

        print( "sorted:", sorted_s )

        print( "pretty printed original: ", end="[")
        linked_insort.pretty_print( original_s )
        print( "pretty printed sorted: ", end="[")
        linked_insort.pretty_print( sorted_s )



if __name__ == "__main__":
    main()