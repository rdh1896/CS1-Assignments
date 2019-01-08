"""
Name: Russell Harvey <rdh1896@rit.edu>
File: moving.py
Assignment: Lab 07
Language: Python3.7
"""

from dataclasses import dataclass

@dataclass
class Box:
    """
    This class when used will create a "Box" which holds the values
    current_weight which is the weight currently in the box, max_weight
    which is the amount of weight the box can hold, and items which is a
    list of items in the box.
    """
    current_weight : int
    max_weight : int
    items : list

@dataclass
class Item:
    """
    This class when used will create an "Item" which holds the values name
    which is the name of the object and weight which is the weight of the
    object.
    """
    name : str
    weight : int

def create_data(file):
    """
    Creates two lists, boxes and items, then reads a file. When it reads the first line,
    it will create a Box dataclass and put it in boxes with a maximum weight of the integer
    being read. After that, it will then read line by line creating Item dataclasses and
    putting them into the items list. The function will then return the boxes and items lists.
    :param file: File being read
    :return: boxes, items
    """
    boxes = []
    items = []
    with open(file) as file:
        line = file.readline()
        line = line.strip()
        for i in line.split(" "):
            boxes.append(Box(0, int(i), []))
        for line in file:
            line = line.strip()
            name, weight = line.split(" ")
            items.append(Item(name, int(weight)))
    return boxes, items

def partition(pivot, lst):
    """
    Takes in a list and a pivot and partitions it based on items greater, less, and equal to
    the pivot value within the list. Returns a tuple with the more, same and less lists. Depends on
    the weight value attached to the terms in the list which are all from an Item dataclass.
    :param pivot: Value being pivoted around
    :param lst: List being partitioned
    :return: more, less, same
    """
    (less, same, more) = ([], [], [])
    for i in lst:
        if i.weight > pivot.weight:
            more.append(i)
        elif i.weight < pivot.weight:
            less.append(i)
        else:
            same.append(i)
    return (more, same, less)

def reverse_quick_sort(lst):
    """
    Takes in a list and sorts it in decreasing order from greatest term to smallest term.
    :param lst: List being sorted
    :return: reverse_quick_sort(more) + same + reverse_quick_sort(less), lst
    """
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        (more, same, less) = partition(pivot, lst)
        return reverse_quick_sort(more) + same + reverse_quick_sort(less)

def roomiest(file):
    """
    Takes in a file with a list of items and boxes and stores items based on which box
    has the most room left in it. The function sorts items in descending order then goes
    through them one by one and puts them in the box with the most space left in it. If an
    item cannot fit in any box, it will be left behind. Prints results.
    :param file: File being read by the function
    :return: None
    """
    boxes = create_data(file)[0]
    items = reverse_quick_sort(create_data(file)[1])
    floor_items = []
    box_count = list(range(len(boxes)))
    for item in items:
        emptiest_box = boxes[0]
        for box in boxes:
            if box.max_weight - box.current_weight >= emptiest_box.max_weight - emptiest_box.current_weight:
                emptiest_box = box
            else:
                pass
        if emptiest_box.max_weight - emptiest_box.current_weight >= item.weight:
                emptiest_box.items = emptiest_box.items + [item]
                emptiest_box.current_weight = emptiest_box.current_weight + item.weight
        else:
            floor_items.append(item)
    print("Results from Greedy Strategy 1")
    if not floor_items:
        print("All items successfully packed into boxes!")
    else:
        print("Unable to pack all items!")
    for i in box_count:
        print("Box", i + 1, "of weight capacity", boxes[i].max_weight, "contains: ")
        item_count = list(range(len(boxes[i].items)))
        for item in item_count:
            print("\t", boxes[i].items[item].name, "of weight", boxes[i].items[item].weight)
    if not floor_items:
        pass
    else:
        for i in floor_items:
            print(i.name, "of weight", i.weight, "got left behind.")

def tightest_fit(file):
    """
    Takes in a file with a list of items and boxes and stores items based on which box
    has the least amount of space for a given item to fit in the box. The function sorts
    items in descending order then goes through them one by one and puts them in the box
    with the least amount of space in it that the item can fit in. If an item cannot fit
    in any box, it will be left behind. Prints results.
    :param file: File being read by the function
    :return: None
    """
    boxes = create_data(file)[0]
    items = reverse_quick_sort(create_data(file)[1])
    floor_items = []
    box_count = list(range(len(boxes)))
    for item in items:
        tightest_box = boxes[0]
        for box in boxes:
            tightest_box_diff = tightest_box.max_weight - tightest_box.current_weight
            box_diff = box.max_weight - box.current_weight
            if item.weight <= tightest_box_diff and item.weight <= box_diff:
                if tightest_box_diff >= box_diff:
                    tightest_box = box
                else:
                    pass
            elif tightest_box_diff <= item.weight <= box_diff:
                tightest_box = box
            else:
                pass
        if tightest_box.max_weight - tightest_box.current_weight >= item.weight:
            tightest_box.items = tightest_box.items + [item]
            tightest_box.current_weight = tightest_box.current_weight + item.weight
        else:
            floor_items.append(item)
    print("Results from Greedy Strategy 2")
    if not floor_items:
        print("All items successfully packed into boxes!")
    else:
        print("Unable to pack all items!")
    for i in box_count:
        print("Box", i + 1, "of weight capacity", boxes[i].max_weight, "contains: ")
        item_count = list(range(len(boxes[i].items)))
        for item in item_count:
            print("\t", boxes[i].items[item].name, "of weight", boxes[i].items[item].weight)
    if not floor_items:
        pass
    else:
        for i in floor_items:
            print(i.name, "of weight", i.weight, "got left behind.")

def one_box(file):
    """
    Takes in a file with a list of items and boxes and stores items box by box depending
    on if the item fits in the box. The function sorts items in descending order then goes
    through them one by one and puts them in the first box that it can fit in. If an item
    cannot fit in any box, it will be left behind. Prints results.
    :param file: File being read by the function
    :return: None
    """
    boxes = create_data(file)[0]
    items = reverse_quick_sort(create_data(file)[1])
    floor_items = []
    box_count = list(range(len(boxes)))
    for item in items:
        for box in boxes:
            if item.weight <= box.max_weight - box.current_weight:
                box.items = box.items + [item]
                box.current_weight = box.current_weight + item.weight
                break
            else:
                pass
        if item not in box.items:
            floor_items.append(item)
    print("Results from Greedy Strategy 3")
    if not floor_items:
        print("All items successfully packed into boxes!")
    else:
        print("Unable to pack all items!")
    for i in box_count:
        print("Box", i + 1, "of weight capacity", boxes[i].max_weight, "contains: ")
        item_count = list(range(len(boxes[i].items)))
        for item in item_count:
            print("\t", boxes[i].items[item].name, "of weight", boxes[i].items[item].weight)
    if not floor_items:
        pass
    else:
        for i in floor_items:
            print(i.name, "of weight", i.weight, "got left behind.")

def main():
    """
    Takes in a file as input, and then runs it through the three greedy strategies
    listed above.
    :return: None
    """
    file = input("Enter data filename: ")
    print("")
    roomiest(file)
    print("")
    tightest_fit(file)
    print("")
    one_box(file)

if __name__ == "__main__":
    main()

