"""
Name: Russell Harvey <rdh1896@rit.edu>
File: tasks.py
Assignment: hw11
Language: Python3.7
"""

from dataclasses import dataclass
from priority_queue import *
import random as rand

@dataclass
class Task:
    """
    Creates a class that stores a "name" and "priority" value.
    Priority must be a integer, name must be a string.
    """
    name : str
    priority: int

def make_task(name, priority):
    """
    Creates an empty Task class.
    :param name: Name stored in the task.
    :param priority: Priority of the task.
    :return: New empty Task class.
    """
    return Task(name, priority)

def test1():
    """
    Tests priority queue using random integers.
    :return: None
    """
    q = make_priority_queue()
    count = 0
    while True:
        if count == 10:
            break
        i = rand.randint(1,10)
        task = "Task" + str(count + 1)
        enqueue(q, Task(task, i))
        count += 1
    print("Created Queue: ", q)
    t = front(q)
    print("Highest priority task is", t.name, "with priority", t.priority)
    t = back(q)
    print("Lowest priority task is", t.name, "with priority", t.priority)
    while not is_empty(q):
        t = front(q)
        dequeue(q)
    if is_empty(q) is True:
        print("Dequeue Success? - True")
    else:
        print("Dequeue Success? - False")

def test2():
    """
    Tests priority queue using integers ascending 1 through 10.
    :return: None
    """
    q = make_priority_queue()
    for i in range(10):
        task = "Task" + str(i+1)
        enqueue(q, Task(task, i + 1))
    print("Created Queue: ", q)
    t = front(q)
    print("Highest priority task is", t.name, "with priority", t.priority)
    t = back(q)
    print("Lowest priority task is", t.name, "with priority", t.priority)
    while not is_empty(q):
        t = front(q)
        dequeue(q)
    if is_empty(q) is True:
        print("Dequeue Success? - True")
    else:
        print("Dequeue Success? - False")

def test3():
    """
    Tests priority queue using 10 instances of the same priority.
    :return: None
    """
    q = make_priority_queue()
    count = 0
    while True:
        if count == 10:
            break
        i = 5
        task = "Task" + str(count + 1)
        enqueue(q, Task(task, i))
        count += 1
    print("Created Queue: ", q)
    t = front(q)
    print("Highest priority task is", t.name, "with priority", t.priority)
    t = back(q)
    print("Lowest priority task is", t.name, "with priority", t.priority)
    while not is_empty(q):
        t = front(q)
        dequeue(q)
    if is_empty(q) is True:
        print("Dequeue Success? - True")
    else:
        print("Dequeue Success? - False")

def test4():
    """
    Tests priority queue using one value.
    :return: None
    """
    q = make_priority_queue()
    enqueue(q, Task("Task1", 3))
    print("Created Queue: ", q)
    t = front(q)
    print("Highest priority task is", t.name, "with priority", t.priority)
    t = back(q)
    print("Lowest priority task is", t.name, "with priority", t.priority)
    while not is_empty(q):
        t = front(q)
        dequeue(q)
    if is_empty(q) is True:
        print("Dequeue Success? - True")
    else:
        print("Dequeue Success? - False")

def test5():
    """
    Tests priority queue using a stair formation of values.
    :return: None
    """
    q = make_priority_queue()
    enqueue(q, Task("Task1", 1))
    enqueue(q, Task("Task2", 2))
    enqueue(q, Task("Task3", 3))
    enqueue(q, Task("Task4", 4))
    enqueue(q, Task("Task5", 5))
    enqueue(q, Task("Task6", 5))
    enqueue(q, Task("Task7", 4))
    enqueue(q, Task("Task8", 3))
    enqueue(q, Task("Task9", 2))
    enqueue(q, Task("Task10", 1))
    print("Created Queue: ", q)
    t = front(q)
    print("Highest priority task is", t.name, "with priority", t.priority)
    t = back(q)
    print("Lowest priority task is", t.name, "with priority", t.priority)
    while not is_empty(q):
        t = front(q)
        dequeue(q)
    if is_empty(q) is True:
        print("Dequeue Success? - True")
    else:
        print("Dequeue Success? - False")

def test_suite():
    """
    Executes all test functions.
    :return: None
    """
    print("Testing Random Integers:")
    test1()
    print("")
    print("Testing Increasing Order:")
    test2()
    print("")
    print("Testing Equal Values:")
    test3()
    print("")
    print("Testing One Value:")
    test4()
    print("")
    print("Testing Stair Sequence:")
    test5()

test_suite()