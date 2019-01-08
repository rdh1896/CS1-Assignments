"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Spellotron
File: punc_handling.py
Language: Python3.7
"""

def punctuation_init(word):
    """
    Takes a word as input and searches it for punctuation. If it finds any form of punctuation,
    it will strip it from the word and store it in the punc_found variable and then store its
    index in the punc_loc variable. The function has unique handling if the word contains apostrophes
    in it so it will not strip them if they are part of the word. When the function completes, it will
    return the fixed word, any punctuation found, and their respective locations.
    :param word: Word being checked for punctuation.
    :return: fixed_word, punc_found, punc_loc
    """
    fixed_word = word
    punc_found = None
    punc_loc = []
    punc = [".", ",", ":", ";", "'", '"', "{", "}", "[", "]", "(", ")", "-", "_", "@", "#", "$", "%", "^", "&", \
            "*", "?", "!", "+", "=", "/", "\\", "‘", "’"]
    counter = 0
    for i in word:
        if i in punc:
            punc_found = []
    for i in word:
        if i in punc:
            if (counter == 1 or counter == len(word) - 2) and len(word) > 2 and (i[0] != "'" and i[0] != '"'):
                if i == "'":
                    counter += 1
                elif i == "’":
                    punc_found.append(i)
                    punc_loc.append(counter)
                    fixed_word = fixed_word.replace(i, "'")
                    counter += 1
                else:
                    punc_found.append(i)
                    punc_loc.append(counter)
                    fixed_word = fixed_word.replace(i, "")
                    counter += 1
            else:
                punc_found.append(i)
                punc_loc.append(counter)
                fixed_word = fixed_word.replace(i, "")
                counter += 1
        else:
            counter += 1
    return fixed_word, punc_found, punc_loc

def find_case(word):
    """
    Locates uppercase characters in a word and replaces them with their lower case
    alternative.
    :param word: Word being checked for case.
    :return: [word, False] if no caps found, [word, True] if caps found.
    """
    if word[0] == word[0].upper():
        return word.lower(), True
    else:
        return word, False

def replace_case(word, switch):
    """
    Takes in a word and a switch variable. If the switch is true, it will convert the
    first letter in word to a capital. If false it will ignore changing the word.
    :param word: Word being changed.
    :param switch: Boolean to determine if the word needs to be changed.
    :return: [word[0].upper() + word[1:]] if True, [word] if False.
    """
    if switch == True:
        return word[0].upper() + word[1:]
    else:
        return word

def replace_punc(word, orig_word, punc, punc_loc):
    """
    Takes in a word, its original form before any changes being made, any punctuation found in it
    and the respective location for each character of punctuation and replaces it back into the word
    after correction of the word. Has handling if the word never had punctuation in it so it doesn't
    break corrected words who never had punctuation to begin with.
    :param word: Word that has been corrected.
    :param orig_word: Word before correction.
    :param punc: Punctuation found in the original word.
    :param punc_loc: Respective location for each piece of punctuation found.
    :return: fixed_word; The complete fixed version of the word with punctuation
    replaced into it.
    """
    strip_orig = orig_word
    replace_word = ""
    counter = 0
    word_counter = 0
    first_letter = 0
    if punc is None:
        return word
    else:
        for ch in range(0, len(orig_word)):
            if orig_word[ch] in punc:
                pass
            else:
                first_letter = ch
                break
        for p in punc:
            strip_orig = strip_orig.replace(p, "")
        if len(word) == len(strip_orig):
            for i in range(0, len(orig_word)):
                    if i in punc_loc:
                        replace_word = replace_word + punc[counter]
                        counter += 1
                    else:
                        replace_word = replace_word + word[word_counter]
                        word_counter += 1
        else:
            pass
        if len(word) != len(strip_orig):
            for term in range(0, len(punc_loc)):
                if len(word) < len(strip_orig):
                    if punc_loc[term] < first_letter:
                        pass
                    else:
                        punc_loc[term] -= 1
                else:
                    if punc_loc[term] < first_letter:
                        pass
                    else:
                        punc_loc[term] += 1
            if len(word) > len(strip_orig):
                for i in range(0, len(orig_word) + 1):
                    if i in punc_loc:
                        replace_word = replace_word + punc[counter]
                        counter += 1
                    else:
                        replace_word = replace_word + word[word_counter]
                        word_counter += 1
            else:
                for i in range(0, len(orig_word) - 1):
                    if i in punc_loc:
                        replace_word = replace_word + punc[counter]
                        counter += 1
                    else:
                        replace_word = replace_word + word[word_counter]
                        word_counter += 1
        else:
            pass
        return replace_word