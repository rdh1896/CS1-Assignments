"""
Name: Russell Harvey <rdh1896@rit.edu>
File: priority_queue.py
Assignment: hw11
Language: Python3.7
"""

from node import Node
from dataclasses import dataclass
from typing import Union

@dataclass(frozen=False)
class PriorityQueue:
    """
    Creates a PriorityQueue class with values "size", "front", and "back".
    "size" must be an integer, "front" can either be a NoneType or a Node, and
    "back" is the same as "front".
    """
    size: int
    front: Union[None, Node]
    back: Union[None, Node]

def make_priority_queue():
    """
    Returns a new priority queue with size initialized to zero and
    the front and back fields initialized to the empty sequence.
    """
    return PriorityQueue(0, None, None)

def is_empty(queue):
    """
    Checks if the priority queue is empty.
    :param queue: Queue being read.
    :return: Boolean True or False
    """
    return queue.front is None

def back(queue):
    """
    Returns the back value of the priority queue.
    :param queue: Queue being read.
    :return: Value of the back of the queue.
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value

def front(queue):
    """
    Returns the front value value of the priority queue.
    :param queue: Queue being read.
    :return: Value of the front of the queue.
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value

def insert_at(queue, node, idx):
    """
    Takes in an index value and inserts a new node at a certain
    index of a priority queue based on the priority of Tasks contained
    in the priority queue. Has handling if a value needs to be inserted
    in the middle of a queue for the priority to be placed correctly.
    Pre-conditions: The inputted queue must contain a linked node structure with
    values that are Tasks that have a priority attribute.
    :param queue: Queue where the new node is being inserted in to.
    :param node: Node being inserted.
    :param idx: Technically the length of the list plus one. Used if the value
    needs to be inserted in the back. This becomes crucial when changing the back
    value of the priority queue in special situations.
    :return: None
    """
    new_node = node
    current_node = queue.front
    while idx != 1:
        if current_node.rest is None:
            break
        elif current_node.value.priority < node.value.priority:
            break
        current_node = current_node.rest
        idx -= 1
    if current_node.value.priority > new_node.value.priority:
        queue.back = new_node
    if current_node.value.priority > new_node.value.priority:
        current_node.rest = new_node
    else:
        current_node.rest = Node(current_node.value, current_node.rest)
        current_node.value = new_node.value
        if idx == 1:
            queue.back = current_node.rest
    queue.size += 1

def indexer(queue, node):
    """
    Counts the index of a queue. In order for it to work properly in my
    program, the index is increased by one.
    :param queue: Queue being read.
    :param node: Helps us find index by counting up to where Node should
    be in the list.
    :return: count
    """
    count = 1
    current_node = queue.front
    while front(queue).priority > node.value.priority:
        if current_node.rest is None:
            break
        current_node = current_node.rest
        count += 1
    return count

def enqueue(queue, element):
    """
    Takes in an element and a queue and places it in a queue based on a certain
    priority value located in a Task class. The higher the priority, the closer the
    element will be placed to the front of the list.
    :param queue: Queue being read.
    :param element: Element we are putting into the queue based on priority.
    :return: None
    """
    new_node = Node(element, None)
    if is_empty(queue):
        queue.front = new_node
        queue.back = new_node
        queue.size = queue.size + 1
    else:
        if front(queue).priority > element.priority:
            idx = indexer(queue, new_node)
            insert_at(queue, new_node, idx)
        else:
            current_node = queue.front
            if current_node.value.priority == new_node.value.priority:
                while current_node.rest is not None:
                    if current_node.value.priority < new_node.value.priority:
                        break
                    current_node = current_node.rest
                if current_node.value.priority == new_node.value.priority:
                    current_node.rest = new_node
                    queue.back = Node(new_node.value, None)
                else:
                    queue.front = Node(queue.front.value, Node(element, current_node))
            else:
                queue.front = Node(element, queue.front)
            queue.size += 1

def dequeue(queue):
    """
    Remove the front element from the queue. (returns removed value)
    Pre-condition: Queue is not empty.
    :param queue: Queue being read.
    :return: removed
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed

