"""
Name: Russell "Kevin" Harvey
Assignment: Lab 08
File: dna.py
Language: Python3.7
"""

from dataclasses import dataclass
from typing import Any, Union
import linked_code as lc

@dataclass (frozen=True)
class LinkNode:
    value : Any
    rest : Union["LinkNode", None]

def convert_to_nodes(dna_string):
    """
    Converts a string into a linked structure.
    :param dna_string: A string of characters corresponding to DNA bases.
    :return: A linked-node data structure representing the input DNA sequence. Each
    character of the input string is represented as a node in the sequence.
    """
    if dna_string == "":
        return None
    else:
        return LinkNode(dna_string[0], convert_to_nodes(dna_string[1:]))

def convert_to_string(dna_seq):
    """
    Converts a linked structure into a string.
    :param dna_seq: A linked-node data structure representing the input DNA sequence.
    :return: A string
    """
    if dna_seq is None:
        return ""
    else:
        return str(dna_seq.value) + convert_to_string(dna_seq.rest)

def is_match(dna_seq1, dna_seq2):
    """
    Checks to see if both sequences are exactly the same as each other.
    :param dna_seq1: A first linked sequence with data nodes representing a DNA sequence.
    :param dna_seq2: A second linked sequence with data nodes representing a DNA sequence.
    :return: Boolean True or  False
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value != dna_seq2.value:
        return False
    else:
        return is_match(dna_seq1.rest, dna_seq2.rest)

def is_pairing(dna_seq1, dna_seq2):
    """
    Checks to see if the values at each index of two different DNA sequences
    are corresponding (i.e. A and T, G and C).
    :param dna_seq1: A first linked sequence with data nodes representing a DNA sequence.
    :param dna_seq2: A first linked sequence with data nodes representing a DNA sequence.
    :return: Boolean True or  False
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value == "G" and dna_seq2.value == "C":
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    elif dna_seq1.value == "C" and dna_seq2.value == "G":
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    elif dna_seq1.value == "A" and dna_seq2.value == "T":
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    elif dna_seq1.value == "T" and dna_seq2.value == "A":
        return is_pairing(dna_seq1.rest,dna_seq2.rest)
    else:
        return False

def is_palindrome(dna_seq):
    """
    Checks to see if the DNA sequence is the same forwards and backwards.
    :param dna_seq: A linked sequence with data nodes representing a DNA sequence.
    :return: Boolean True or  False
    """
    new_seq = lc.reverse_iter(dna_seq)
    return is_match(dna_seq, new_seq)

def substitution(dna_seq, idx, base):
    """
    Takes a DNA sequence and substitutes a new base in at a certain index.
    :param dna_seq: The sequence in which the substitution mutation occurs.
    :param idx: Index where the substitution occurs.
    :param base: The new base to be substituted at a specific index.
    :return: A new linked sequence that represents the DNA strand after the
    substitution mutation has occurred.
    """
    if dna_seq is None or idx < 0:
        raise IndexError("index out of bounds in substitution")
    elif idx == 0:
        return lc.concatenate(LinkNode(base, None), dna_seq.rest)
    else:
        return LinkNode(dna_seq.value, substitution(dna_seq.rest,idx-1,base))

def insertion(dna_seq1, dna_seq2, idx):
    """
    Inserts a new sequence at a given index of an original sequence.
    :param dna_seq1: The first sequence into which the second sequence is inserted.
    :param dna_seq2: The second sequence, which is inserted into the first.
    :param idx: The index before which the insertion occurs.
    :return: A new linked sequence that represents the resulting DNA strand after
    dna_seq2 has been inserted in its entirety just before idx in dna_seq1.
    """
    if idx == 0:
        return lc.concatenate(dna_seq2, dna_seq1)
    elif dna_seq1 is None:
        raise IndexError("Error: Index out of range.")
    elif idx < 0:
        raise IndexError("Error: Index out of range.")
    else:
        return LinkNode(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx - 1))

def deletion(dna_seq, idx, segment_size):
    """
    Deletes a specific sized segment in a sequence at a certain index.
    :param dna_seq:The sequence from which a segment of elements will be deleted.
    :param idx: The index at which deletion begins.
    :param segment_size: The number of elements to be deleted.
    :return: A new linked sequence that represents the resulting DNA strand after the specified segment of
    elements have been removed from dna_seq.
    """
    if idx == 0:
        if segment_size == 0:
            return dna_seq
        else:
            return deletion(dna_seq.rest,idx,segment_size-1)
    else:
        if dna_seq is not None:
            return LinkNode(dna_seq.value ,deletion(dna_seq.rest,idx-1,segment_size))
        else:
            return None

def duplication(dna_seq, idx, segment_size, count = 0):
    """
    Duplicates a segment of a sequence and inserts it right after the end of the segment.
    :param dna_seq: The sequence from which a segment of elements will be copied.
    :param idx: The index at which the segment to be duplicated begins.
    :param segment_size: The number of elements to be duplicated.
    :param count: Way of keeping track of what processes have been done.
    :return: A new linked sequence that represents the resulting DNA strand
    after the specified segment of elements from dna_seq have been copied.
    """
    leng = lc.length_rec(dna_seq)
    if segment_size == 0 and idx > leng:
        return dna_seq
    elif idx + segment_size > leng:
        raise IndexError("Error: Index out of range.")
    elif segment_size == 0 and count == 0:
        return dna_seq
    elif idx==0 and count == 0:
        return insertion(dna_seq, duplication(dna_seq, idx, segment_size, 1), idx)
    elif idx == 0:
        if segment_size != 0:
            return LinkNode(dna_seq.value, duplication(dna_seq.rest, idx, segment_size - 1, 1))
        else:
            pass
    else:
        if count == 0:
            return insertion(dna_seq, duplication(dna_seq.rest, idx-1, segment_size, 1), idx)
        else:
            return duplication(dna_seq.rest, idx-1, segment_size, 1)
