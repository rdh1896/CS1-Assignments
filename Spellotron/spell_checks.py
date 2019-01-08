"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Spellotron
File: spell_checks.py
Language: Python3.7
"""

from create_word_dictionary import create_adjacent_keys

def adjacent_error(word, word_dict):
    """
    Checks for an adjacent error in a word. If the word is found to have an adjacency error,
    the function will return the corrected word. If there is no error to be found, the function
    will return None. Has handling if punctuation that is an apostrophe is found in a word and ignores
    it so it does not brick the function.
    :param word: Word being checked for adjacency error.
    :param word_dict: American English Dictionary.
    :return: new_word or None
    """
    adj = create_adjacent_keys()
    for i in range(0, len(word)):
        switch = False
        if word[i] == "'" or word[i] == "’" or word[i] == "‘":
            pass
        elif word[i] == word[i].upper():
            c = word[i].lower()
            switch = True
        else:
            c = word[i]
        for term in adj[c]:
            if switch is True:
                new_word = word[:i] + term.upper() + word[i+1:]
            else:
                new_word = word[:i] + term + word[i+1:]
            if len(new_word) == 1:
                if new_word in word_dict[new_word[0]][new_word[0]]:
                    return new_word
                else:
                    pass
            elif new_word[1] in word_dict[new_word[0]]:
                if new_word in word_dict[new_word[0]][new_word[1]]:
                    return new_word
                else:
                    pass
            else:
                pass
    return None

def missing_word(word, word_dict):
    """
    Checks if a word is missing any character. If it is, it will return the corrected word.
    Otherwise it will return None.
    :param word: Word being corrected.
    :param word_dict: American English Dictionary
    :return: new_word or None
    """
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
            "v", "w", "x", "y", "z"]
    for i in range(0, len(word)+1):
        for term in alph:
            new_word = word[:i] + term + word[i:]
            if new_word[1] in word_dict[new_word[0]]:
                if new_word in word_dict[new_word[0]][new_word[1]]:
                    return new_word
            else:
                pass
    return None

def extra_word(word, word_dict):
    """
    Checks if a word has extra characters. If it is, it will return the corrected word.
    Otherwise it will return None.
    :param word: Word being corrected.
    :param word_dict: American English Dictionary
    :return: new_word or None
    """
    for i in range(0, len(word)+1):
        new_word = word[:i] + word[i+1:]
        if len(new_word) == 1:
            if new_word in word_dict[new_word[0]][new_word[0]]:
                return new_word
        elif new_word[1] in word_dict[new_word[0]]:
            if new_word in word_dict[new_word[0]][new_word[1]]:
                return new_word
        else:
            pass

def is_word(word, word_dict):
        """
        Checks to see if the word is in the American English dictionary both with case in it and with
        all case lowered. If the word is found, the function will return True. If it is not found, the
        function will return False.
        :param word: Word being checked.
        :param word_dict: American English Dictionary
        :return: True, False
        """
        punc = [".", ",", ":", ";", "'", '"', "{", "}", "[", "]", "(", ")", "-", "_", "@", "#", "$", "%", "^", "&", \
                "*", "?", "!", "+", "=", "/", "\\", "‘", "’"]
        if word[0] in punc or word[1] in punc:
            return False
        elif word[1] in word_dict[word[0]]:
            if word in word_dict[word[0]][word[1]]:
                return True
            else:
                temp = word.lower()
                if temp[1] in word_dict[temp[0]]:
                    if temp in word_dict[temp[0]][temp[1]]:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            temp = word.lower()
            if temp[1] in word_dict[temp[0]]:
                if temp in word_dict[temp[0]][temp[1]]:
                    return True
                else:
                    return False
            else:
                return False