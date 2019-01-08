"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Spellotron
File: create_word_dictionary.py
Language: Python3.7
"""

LEGAL_WORD_FILE = "american-english.txt"
KEY_ADJACENCY_FILE = "keyboard-letters.txt"

def create_dictionary():
    """
    Creates a word dictionary sorted by the first two letters in a word.
    The dictionary is nested so for every key in the main dictionary, there
    is another dictionary with more keys. This helps our efficiency. The function
    uses the american-english.txt file as a reference to build the dictionary.
    :return: words; A dictionary containing all words in american-english.txt
    """
    file = open(LEGAL_WORD_FILE, encoding="utf-8")
    words = {}
    for line in file:
        line = line.strip()
        word = line
        if word[0] in words:
            if len(word) == 1:
                words[word[0]][word[0]].append(line)
            elif word[1] == "'":
                words[word[0]][word[0]].append(line)
            else:
                if word[1] in words[word[0]]:
                    words[word[0]][word[1]].append(line)
                else:
                    words[word[0]][word[1]] = [line]
        else:
            words[word[0]] = {}
            if len(word) == 1:
                words[word[0]][word[0]] = [line]
            elif word[1] == "'":
                word[word[0]][word[0]].append(line)
            else:
                words[word[0]][word[1]] = [line]
    return words

def create_adjacent_keys():
    """
    Creates a dictionary from the keyboard-letters.txt file where the first character
    on each line is stored as a key and the following values are stored in a list as
    the key value. This is to be used for adjacent key errors.
    :return: adj; A dictionary containing every alphabetic character found on a keyboard
    followed by the keys adjacent to each character.
    """
    file = open(KEY_ADJACENCY_FILE, encoding="UTF-8")
    adj = {}
    for line in file:
        line = line.strip().split()
        adj[line[0]] = []
        for i in range(1, len(line)):
            adj[line[0]].append(line[i])
    return adj