"""
Name: Russell Harvey <rdh1896@rit.edu>
Assignment: Spellotron
File: words_mode.py
Language: Python3.7
"""

from create_word_dictionary import *
from spell_checks import *
from punc_handling import *
import time

GLOBAL_DICT = create_dictionary()

def words_algorithm(text, mispelled_words, unknown_words, word_tally):
    """
    Takes in a list of strings and spell checks each term.
    ---------------------------------------------------------------------------------
    Has cases for the following:
    1. If the word has only one character that is a letter
    2. If the word has only one letter, but has punctuation.
    3. If the word only has numbers (and/or punctuation).
    4. If the word has punctuation as its second index.
        This is for words such as "I'm" where my dictionary will encounter
        a key error because no punctuation is included in it.
    5. If all other cases are false it will begin a true spell correction process.
    ---------------------------------------------------------------------------------
    True Spell Correction Process:
        Step 1.1: Check if the word is legal. If true, skip to step 2.1.
        Step 1.2: Remove punctuation from the word. If word is legal, skip to step 2.1.
        Step 1.3: Spell check word. If word is legal, skip to step 2.2.
        Step 1.4: Remove case from word then spell check again. If word is legal, skip
                  to step 2.2.
        Step 1.5: If word cannot be found legal, append original word to unknown.
        Step 2.1: If word is found legal you can ignore it in words mode.
        Step 2.2: If the word is found to be illegal. The word will be returned corrected
                  with the case and punctuation being replaced if needed. The original
                  word needs to be appended to corrected words.
    For the other cases, the correction process follows a similar pattern but varied
    slightly so errors are not encountered.
    ----------------------------------------------------------------------------------
    When completed the function will return any misspelled words, unknown words, the tally
    of total words, and the resulting string after correction (corrected words).
    :param text: List being spell checked.
    :param mispelled_words: Any mispelled words in the list.
    :param unknown_words: Any unknown words in the list.
    :param word_tally: Total amount of words in the list.
    :return: mispelled_words, unknown_words, words_tally, corrected_words
    """
    counter = 0
    punc_data = None
    case_data = "", False
    current_word = None
    corrected_words = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    punc = [".", ",", ":", ";", "'", '"', "{", "}", "[", "]", "(", ")", "-", "_", "@", "#", "$", "%", "^", "&", \
            "*", "?", "!", "+", "=", "/", "\\", "‘", "’"]
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
            "v", "w", "x", "y", "z"]
    for i in text:
        word_tally += 1
        current_word = i
        single_ch_count = 0
        num_count = 0
        for ch in i:
            if ch.lower() in alph:
                single_ch_count += 1
            elif ch in numbers:
                num_count += 1
            else:
                pass
        if single_ch_count == 1 and len(i) == 1:
            if i in GLOBAL_DICT[i[0]][i[0]]:
                pass
            else:
                check = adjacent_error(i, GLOBAL_DICT)
                if check is None:
                    unknown_words.append(current_word)
                else:
                    mispelled_words.append(current_word)
                    corrected_words.append(check)
        elif single_ch_count == 1 and num_count == 0:
            punc_data = punctuation_init(i)
            i = punc_data[0]
            if i in GLOBAL_DICT[i[0]][i[0]]:
                pass
            else:
                check = adjacent_error(i, GLOBAL_DICT)
                if check is None:
                    check_two = missing_word(i, GLOBAL_DICT)
                    if check_two is None:
                        check_three = extra_word(i, GLOBAL_DICT)
                        if check_three is None:
                            unknown_words.append(current_word)
                        else:
                            check_three = replace_case(check_three, case_data[1])
                            check_three = replace_punc(check_three, current_word, punc_data[1],
                                                       punc_data[2])
                            mispelled_words.append(current_word)
                            corrected_words.append(check_three)
                    else:
                        check_two = replace_case(check_two, case_data[1])
                        check_two = replace_punc(check_two, current_word, punc_data[1], punc_data[2])
                        mispelled_words.append(current_word)
                        corrected_words.append(check_two)
                else:
                    check = replace_case(check, case_data[1])
                    check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                    mispelled_words.append(current_word)
                    corrected_words.append(check)
        elif single_ch_count == 0 or num_count > 0:
            unknown_words.append(i)
        elif i[1] in punc and (i[0].lower() in alph and i[2].lower() in alph):
            if i in GLOBAL_DICT[i[0]][i[0]]:
                pass
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if is_word(i, GLOBAL_DICT):
                    pass
                else:
                    case_data = find_case(i)
                    i = case_data[0]
                    if i[1] in GLOBAL_DICT[i[0]]:
                        if i in GLOBAL_DICT[i[0]][i[1]]:
                            pass
                    else:
                        check = adjacent_error(i, GLOBAL_DICT)
                        if check is None:
                            check_two = missing_word(i, GLOBAL_DICT)
                            if check_two is None:
                                check_three = extra_word(i, GLOBAL_DICT)
                                if check_three is None:
                                    unknown_words.append(current_word)
                                else:
                                    check_three = replace_case(check_three, case_data[1])
                                    check_three = replace_punc(check_three, current_word, punc_data[1],
                                                               punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check_three)
                            else:
                                check_two = replace_case(check_two, case_data[1])
                                check_two = replace_punc(check_two, current_word, punc_data[1], punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check_two)
                        else:
                            check = replace_case(check, case_data[1])
                            check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                            mispelled_words.append(current_word)
                            corrected_words.append(check)
        else:
            if is_word(i, GLOBAL_DICT):
                pass
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if is_word(i, GLOBAL_DICT):
                    pass
                else:
                    check = adjacent_error(i, GLOBAL_DICT)
                    if check is None:
                        check_two = missing_word(i, GLOBAL_DICT)
                        if check_two is None:
                            check_three = extra_word(i, GLOBAL_DICT)
                            if check_three is None:
                                case_data = find_case(i)
                                i = case_data[0]
                                if is_word(i, GLOBAL_DICT):
                                    pass
                                else:
                                    check = adjacent_error(i, GLOBAL_DICT)
                                    if check is None:
                                        check_two = missing_word(i, GLOBAL_DICT)
                                        if check_two is None:
                                            check_three = extra_word(i, GLOBAL_DICT)
                                            if check_three is None:
                                                unknown_words.append(current_word)
                                            else:
                                                check_three = replace_case(check_three, case_data[1])
                                                check_three = replace_punc(check_three, current_word, punc_data[1],
                                                                           punc_data[2])
                                                mispelled_words.append(current_word)
                                                corrected_words.append(check_three)
                                        else:
                                            check_two = replace_case(check_two, case_data[1])
                                            check_two = replace_punc(check_two, current_word, punc_data[1],
                                                                     punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_two)
                                    else:
                                        check = replace_case(check, case_data[1])
                                        check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check)
                            else:
                                check_three = replace_case(check_three, case_data[1])
                                check_three = replace_punc(check_three, current_word, punc_data[1],
                                                           punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check_three)
                        else:
                            check_two = replace_case(check_two, case_data[1])
                            check_two = replace_punc(check_two, current_word, punc_data[1], punc_data[2])
                            mispelled_words.append(current_word)
                            corrected_words.append(check_two)
                    else:
                        check = replace_case(check, case_data[1])
                        check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                        mispelled_words.append(current_word)
                        corrected_words.append(check)
    return mispelled_words, unknown_words, word_tally, corrected_words

def words_file_read(file):
    """
    Takes in a file and spell checks it. Reports every word corrected word
    as well as a list of unknown and mispelled words along with the total
    amount of words in the file. Also reports how long it took to run the
    process.
    :param file: File being spell corrected.
    :return: None
    """
    start = time.time()
    document = open(file, encoding="UTF-8")
    unknown_words = []
    mispelled_words = []
    word_tally = 0
    corrected_words = []
    print("")
    for line in document:
        print(line, end="")
        line = line.split()
        if line == "":
            pass
        results = words_algorithm(line, mispelled_words, unknown_words, word_tally)
        mispelled_words = results[0]
        unknown_words = results[1]
        word_tally = results[2]
        corrected_words = corrected_words + results[3]
    print("\n")
    for i in range(0, len(corrected_words)):
        print(mispelled_words[i], "->", corrected_words[i])
    print("")
    print("")
    print("")
    print(word_tally, "word(s) read from file.")
    print("")
    print("Misspelled Words: ", mispelled_words)
    print("")
    print("Unknown Words: ", unknown_words)
    end = time.time()
    print("Time Elapsed:", end - start)

def words_mode():
    """
    Takes in an input and spell checks it. Reports every word corrected word
    as well as a list of unknown and mispelled words along with the total
    amount of words in the file. Also reports how long it took to run the
    process.
    :return: None
    """
    text = input()
    start = time.time()
    text = text.split()
    unknown_words = []
    mispelled_words = []
    word_tally = 0
    corrected_words = []
    results = words_algorithm(text, mispelled_words, unknown_words, word_tally)
    mispelled_words = results[0]
    unknown_words = results[1]
    word_tally = results[2]
    corrected_words = corrected_words + results[3]
    for i in range(0, len(corrected_words)):
        print(mispelled_words[i], "->", corrected_words[i])
    print("")
    print("")
    print("")
    print(word_tally, "word(s) read from file.")
    print("")
    print("Misspelled Words: ", mispelled_words)
    print("")
    print("Unknown Words: ", unknown_words)
    print("")
    end = time.time()
    print("Time Elapsed:", end - start)