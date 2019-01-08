"""
file: linked_insort.py
author: Russell Harvey <rdh1896@rit.edu>
description: homework
"""

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
    rest: Union[None, "LinkNode"]

def insert( value, lnk ):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk is None:
        return LinkNode(value, None)
    elif lnk.value > value:
        return LinkNode(value, lnk)
    elif lnk.value < 0 and value < 0:
        if lnk.value < value:
            return LinkNode(value, lnk)
        else:
            pass
    else:
        return LinkNode(lnk.value, insert(value, lnk.rest))

def insort( lnk ):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    value = lnk.value
    seq = None
    holder = lnk.rest
    while True:
        if value is None:
            break
        else:
            seq = insert(value, seq)
            if holder is None:
                value = None
            else:
                value = holder.value
                holder = holder.rest
    return seq

def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    if lnk is None:
        print()
    else:
        if lnk.rest is None:
            print(lnk.value, end="]")
        else:
            print(lnk.value, end=", ")
        pretty_print(lnk.rest)
