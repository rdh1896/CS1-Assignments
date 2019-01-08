"""
Name: Aaron Blondale
Language: Python 3.7
File: dna.py
"""

from dataclasses import dataclass
from typing import Any, Union
import linked_code


@dataclass(frozen=True)
class LinkNode:
    """
    An object type to hold any kind of data that can be put into a sequence
    """
    value: Any
    rest: Union[None, "LinkNode"]


def convert_to_nodes(dna_string):
    """
    Converts a given string into a linked node.
    :param dna_string: A string of characters corresponding to DNA bases.
    :return: A linked-node data structure representing the input DNA sequence. Each
    character of the input string is represented as a node in the sequence.
    """
    if len(dna_string) == 0:
        return None
    else:
        return LinkNode(dna_string[0], convert_to_nodes(dna_string[1:]))


def convert_to_string(dna_seq):
    """
    converts the contents of a node to a string.
    :param dna_seq: A linked-node data structure representing the input DNA sequence.
    :return: A String
    """
    if dna_seq is None:
        return ""
    else:
        return dna_seq.value + convert_to_string(dna_seq.rest)


def is_match(dna_seq1, dna_seq2):
    """
    Checks to see if 2 DNA sequences are the same.
    :param dna_seq1: a first linked sequence with data nodes representing a DNA sequence
    :param dna_seq2: a second linked sequence with data nodes representing a DNA sequence
    :return: boolean, True or  False
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value == dna_seq2.value:
        return is_match(dna_seq1.rest, dna_seq2.rest)
    else:
        return False


def is_pairing(dna_seq1, dna_seq2):
    """
    Checks to see if two DNA sequences match with one another.
    :param dna_seq1: a first linked sequence with data nodes representing a DNA sequence
    :param dna_seq2: a first linked sequence with data nodes representing a DNA sequence
    :return: boolean, True or  False
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value == "A" and dna_seq2.value == "T":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    elif dna_seq1.value == "T" and dna_seq2.value == "A":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    elif dna_seq1.value == "G" and dna_seq2.value == "C":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    elif dna_seq1.value == "C" and dna_seq2.value == "G":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    else:
        return False


def is_palindrome(dna_seq):
    """
    Checks to see if the dna sequence is a palindrome.
    :param dna_seq: a linked sequence with data nodes representing a DNA sequence
    :return: boolean, True or  False
    """
    n2 = linked_code.reverse_tail_rec(dna_seq)
    return is_match(dna_seq, n2)


def substitution(dna_seq1, idx, base):
    """
    
    :param dna_seq1: 
    :param idx: 
    :param base: 
    :return: 
    """
    if dna_seq1 is None or idx < 0:
        raise IndexError("index out of bounds in substitution")
    elif idx == 0:
        x = LinkNode(base,None)
        return linked_code.concatenate(x, dna_seq1.rest)
    else:
        return LinkNode(dna_seq1.value, substitution(dna_seq1.rest, idx - 1, base))


def insertion(n1, n2, i):
    if i == 0:
        return linked_code.concatenate(n2,n1)
    elif n1 is None or i < 0:
        raise IndexError("index out of bounds in insertion")
    else:
        return LinkNode(n1.value,insertion(n1.rest,n2,i-1))


def deletion(node, i, size):
    if i == 0:
        if size == 0:
            return node
        else:
            return deletion(node.rest,i,size-1)
    else:
        if node is not None:
            return LinkNode(node.value ,deletion(node.rest,i-1,size))
        else:
            return None

def duplication(dna_seq, idx, segment_size, acc = 0):
    length = linked_code.length_tail_rec(dna_seq)
    if segment_size == 0 and (idx) > length:
        return dna_seq
    elif idx + segment_size > length:
        raise IndexError("")
    elif segment_size == 0 and acc == 0:
        return dna_seq
    elif idx==0 and acc == 0:
        return insertion(dna_seq, duplication(dna_seq, idx, segment_size, 1), idx)
    elif idx == 0:
        if segment_size == 0:
            pass
        else:
            return LinkNode(dna_seq.value, duplication(dna_seq.rest, idx, segment_size - 1, 1))
    else:
        if acc == 0:
            return insertion(dna_seq, duplication(dna_seq.rest, idx-1, segment_size, 1), idx)
        else:
            return duplication(dna_seq.rest, idx-1, segment_size, 1)