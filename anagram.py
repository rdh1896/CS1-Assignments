"""
Name: Russell Harvey <rdh1896@rit.edu>
File: anagram.py
Assignment: hw09
Language: Python3.7
"""

def create_dictionary():
    """
    Takes in the "american-english.txt" file and converts it into a dictionary where
    all strings that have the exact same characters (order does not matter) will be
    stored in a list as the value for a key that would be the characters in the strings
    of the same characters sorted alphanumerically. For example, the characters "aet"
    as a key would store ["eat" , "ate", "tea", "eta"] for its value.
    :return: words
    """
    file = open("american-english.txt", encoding="utf-8")
    words = {}
    for line in file:
        line = line.strip()
        lst = []
        lst += line
        lst.sort()
        word = "".join(lst)
        if word in words:
            words[word].append(line)
        else:
            words[word] = [line]
    return words

def display_anagrams():
    """
    Takes in any string as an input and displays all anagrams for that string. If the
    user does input a string, it will recall the function after the task has been completed.
    If the user does not input a string, it will pass and terminate the function.
    :return: None
    """
    string = input("Enter input string (hit enter to go to Task 3): ")
    if string != "":
        words = create_dictionary()
        lst = []
        lst += string
        lst.sort()
        sorted_word = "".join(lst)
        if sorted_word in words:
            print("Corresponding words:", words[sorted_word])
        else:
            print("No anagrams for: ", string)
        display_anagrams()
    else:
        print("")

def max_size_list():
    """
    Takes in any number that corresponds with the length of a word. The function then
    iterates over the dictionary created in the create_dictionary() function and finds
    which string of the desired length has the most anagrams and displays how many anagrams
    and prints them. If the user does input a string, it will recall the function after the
    task has been completed. If the user does not input a string, it will pass and terminate
    the function.
    :return:
    """
    num = input("Enter word length (hit enter key to go to Task 4): ")
    if num != "":
        count = int(num)
        words = create_dictionary()
        best = 0
        current_key = None
        for key in words:
            if len(key) == count:
                if len(words[key]) > best:
                    best = len(words[key])
                    current_key = words[key]
                elif len(words[key]) < best:
                    pass
                else:
                    best = len(words[key])
                    current_key = words[key]
            else:
                pass
        print("Max anagrams for length",count,":", best)
        print("Anagram list: ", current_key)
        max_size_list()
    else:
        print("")

def find_jumble():
    """
    Takes in a number that corresponds to the length of a word. The function will then iterate
    over the dictionary created by create_dictionary() and will increment a "tally" variable
    that will count how many terms are good jumble words in the list. To be a good jumble word,
    any key in the dictionary must only have one value in its list. If the user does input a string,
    it will recall the function after the task has been completed. If the user does not input a
    string, it will pass and terminate the function.
    :return: None
    """
    num = input("Enter word length (hit enter key to quit): ")
    if num != "":
        count = int(num)
        words = create_dictionary()
        target = 1
        tally = 0
        for key in words:
            if len(key) == count:
                if len(words[key]) > target:
                    pass
                elif len(words[key]) < target:
                    pass
                else:
                    tally += 1
            else:
                pass
        print("Maximum jumble usable words for length", count, ": ", tally)
        find_jumble()
    else:
        print("")

def main():
    """
    Simply just runs display_anagrams(), max_size_list(), and find_jumble() in a row. Because of
    the intrinsic recall feature in each function, every time a value is inputted into the terminal
    the function will recall itself. If nothing is entered and the enter key is hit, it will move on
    to the next function in the list.
    :return: None
    """
    display_anagrams()
    max_size_list()
    find_jumble()

main()








