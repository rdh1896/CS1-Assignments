def words_algorithm(text, mispelled_words, unknown_words, word_tally):
    counter = 0
    punc_data = None
    case_data = None
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
        if len(i) == 1 and not (i[0] in numbers or i[0] in punc):
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
                    unknown_words.append(current_word)
                else:
                    replace_punc(i, current_word, punc_data[1], punc_data[2])
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
                if i in GLOBAL_DICT[i[0]][i[1]]:
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
        elif i[0] in numbers or i[0] in punc:
            if i[0] in numbers:
                pass
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if i[1] in GLOBAL_DICT[i[0]]:
                    if i in GLOBAL_DICT[i[0]][i[1]]:
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
                                            check_three = replace_punc(check_three, current_word, punc_data[1], punc_data[2])
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
                        check = adjacent_error(i, GLOBAL_DICT)
                        if check is None:
                            check_two = missing_word(i, GLOBAL_DICT)
                            if check_two is None:
                                check_three = extra_word(i, GLOBAL_DICT)
                                if check_three is None:
                                    unknown_words.append(current_word)
                                else:
                                    check_three = replace_case(check_three, case_data[1])
                                    check_three = replace_punc(check_three, current_word, punc_data[1], punc_data[2])
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
        elif i[1] in GLOBAL_DICT[i[0]]:
            if i in GLOBAL_DICT[i[0]][i[1]]:
                pass
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if i[1] in GLOBAL_DICT[i[0]]:
                    if i in GLOBAL_DICT[i[0]][i[1]]:
                        pass
                    else:
                        if i[0] == i[0].upper():
                            case_data = i, False
                            if i[1] in GLOBAL_DICT[i[0]]:
                                temp = i.lower()
                                if i in GLOBAL_DICT[i[0]][i[1]]:
                                    pass
                                elif temp[1] in GLOBAL_DICT[temp[0]]:
                                    if temp in GLOBAL_DICT[temp[0]][temp[1]]:
                                        pass
                                else:
                                    check = adjacent_error(i, GLOBAL_DICT)
                                    if check is None:
                                        check_two = missing_word(i, GLOBAL_DICT)
                                        if check_two is None:
                                            check_three = extra_word(i, GLOBAL_DICT)
                                            if check_three is None:
                                                check = adjacent_error(temp, GLOBAL_DICT)
                                                if check is None:
                                                    check_two = missing_word(temp, GLOBAL_DICT)
                                                    if check_two is None:
                                                        check_three = extra_word(temp, GLOBAL_DICT)
                                                        if check_three is None:
                                                            unknown_words.append(current_word)
                                                        else:
                                                            check_three = replace_case(check_three, case_data[1])
                                                            check_three = replace_punc(check_three, current_word, \
                                                                                       punc_data[1], punc_data[2])
                                                            mispelled_words.append(current_word)
                                                            corrected_words.append(check_three)
                                                    else:
                                                        check_two = replace_case(check_two, case_data[1])
                                                        check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                                 punc_data[2])
                                                        mispelled_words.append(current_word)
                                                        corrected_words.append(check_two)
                                                else:
                                                    check = replace_case(check, case_data[1])
                                                    check = replace_punc(check, current_word, punc_data[1],
                                                                         punc_data[2])
                                                    mispelled_words.append(current_word)
                                                    corrected_words.append(check)
                                            else:
                                                check_three = replace_case(check_three, case_data[1])
                                                check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                           punc_data[2])
                                                mispelled_words.append(current_word)
                                                corrected_words.append(check_three)
                                        else:
                                            check_two = replace_case(check_two, case_data[1])
                                            check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                     punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_two)
                                    else:
                                        check = replace_case(check, case_data[1])
                                        check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check)
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
                                                check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                               punc_data[2])
                                                mispelled_words.append(current_word)
                                                corrected_words.append(check_three)
                                        else:
                                            check_two = replace_case(check_two, case_data[1])
                                            check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                     punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_two)
                                    else:
                                        check = replace_case(check, case_data[1])
                                        check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check)
        else:
            punc_data = punctuation_init(i)
            i = punc_data[0]
            if i[1] in GLOBAL_DICT[i[0]]:
                if i in GLOBAL_DICT[i[0]][i[1]]:
                    pass
                else:
                    if i[0] == i[0].upper():
                        case_data = i, False
                        if i[1] in GLOBAL_DICT[i[0]]:
                            temp = i.lower()
                            if i in GLOBAL_DICT[i[0]][i[1]]:
                                pass
                            elif temp in GLOBAL_DICT[temp[0]][temp[1]]:
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
                                            check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                       punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_three)
                                    else:
                                        check_two = replace_case(check_two, case_data[1])
                                        check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                 punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_two)
                                else:
                                    check = replace_case(check, case_data[1])
                                    check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check)
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
                                            check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                       punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_three)
                                    else:
                                        check_two = replace_case(check_two, case_data[1])
                                        check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                 punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_two)
                                else:
                                    check = replace_case(check, case_data[1])
                                    check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check)
            else:
                if i[0] == i[0].upper():
                    case_data = i, False
                    if i[1] in GLOBAL_DICT[i[0]]:
                        temp = i.lower()
                        if i in GLOBAL_DICT[i[0]][i[1]]:
                            pass
                        elif temp in GLOBAL_DICT[temp[0]][temp[1]]:
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
                                        check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                   punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_three)
                                else:
                                    check_two = replace_case(check_two, case_data[1])
                                    check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                             punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check_two)
                            else:
                                check = replace_case(check, case_data[1])
                                check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check)
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
                                        check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                   punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_three)
                                else:
                                    check_two = replace_case(check_two, case_data[1])
                                    check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                             punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check_two)
                            else:
                                check = replace_case(check, case_data[1])
                                check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check)
    return mispelled_words, unknown_words, word_tally, corrected_words

def lines_algorith(text, mispelled_words, unknown_words, word_tally):
    counter = 0
    punc_data = None
    case_data = None
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
        if len(i) == 1 and not (i[0] in numbers or i[0] in punc):
            if i in GLOBAL_DICT[i[0]][i[0]]:
                corrected_words.append(i)
            else:
                check = adjacent_error(i, GLOBAL_DICT)
                if check is None:
                    unknown_words.append(current_word)
                    corrected_words.append(current_word)
                else:
                    mispelled_words.append(current_word)
                    corrected_words.append(check)
        elif single_ch_count == 1 and num_count == 0:
            punc_data = punctuation_init(i)
            i = punc_data[0]
            if i in GLOBAL_DICT[i[0]][i[0]]:
                i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                corrected_words.append(i)
            else:
                check = adjacent_error(i, GLOBAL_DICT)
                if check is None:
                    unknown_words.append(current_word)
                    corrected_words.append(current_word)
                else:
                    replace_punc(i, current_word, punc_data[1], punc_data[2])
                    mispelled_words.append(current_word)
                    corrected_words.append(check)
        elif (single_ch_count == 1) and (num_count > 0):
            corrected_words.append(i)
            unknown_words.append(i)
        elif single_ch_count == 0:
            corrected_words.append(i)
            unknown_words.append(i)
        elif i[1] in punc and (i[0].lower() in alph and i[2].lower() in alph):
            if i in GLOBAL_DICT[i[0]][i[0]]:
                corrected_words.append(i)
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if i in GLOBAL_DICT[i[0]][i[1]]:
                    i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                    corrected_words.append(i)
                else:
                    case_data = find_case(i)
                    i = case_data[0]
                    if i[1] in GLOBAL_DICT[i[0]]:
                        if i in GLOBAL_DICT[i[0]][i[1]]:
                            corrected_words.append(i)
                    else:
                        check = adjacent_error(i, GLOBAL_DICT)
                        if check is None:
                            check_two = missing_word(i, GLOBAL_DICT)
                            if check_two is None:
                                check_three = extra_word(i, GLOBAL_DICT)
                                if check_three is None:
                                    unknown_words.append(current_word)
                                    corrected_words.append(current_word)
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
        elif i[0] in numbers or i[0] in punc:
            if i[0] in numbers:
                corrected_words.append(i)
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if i[1] in GLOBAL_DICT[i[0]]:
                    if i in GLOBAL_DICT[i[0]][i[1]]:
                        i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                        corrected_words.append(i)
                    else:
                        case_data = find_case(i)
                        i = case_data[0]
                        if i[1] in GLOBAL_DICT[i[0]]:
                            if i in GLOBAL_DICT[i[0]][i[1]]:
                                corrected_words.append(i)
                            else:
                                check = adjacent_error(i, GLOBAL_DICT)
                                if check is None:
                                    check_two = missing_word(i, GLOBAL_DICT)
                                    if check_two is None:
                                        check_three = extra_word(i, GLOBAL_DICT)
                                        if check_three is None:
                                            unknown_words.append(current_word)
                                            corrected_words.append(current_word)
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
                    case_data = find_case(i)
                    i = case_data[0]
                    if i[1] in GLOBAL_DICT[i[0]]:
                        if i in GLOBAL_DICT[i[0]][i[1]]:
                            i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                            corrected_words.append(i)
                        else:
                            check = adjacent_error(i, GLOBAL_DICT)
                            if check is None:
                                check_two = missing_word(i, GLOBAL_DICT)
                                if check_two is None:
                                    check_three = extra_word(i, GLOBAL_DICT)
                                    if check_three is None:
                                        unknown_words.append(current_word)
                                        corrected_words.append(current_word)
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
                        check = adjacent_error(i, GLOBAL_DICT)
                        if check is None:
                            check_two = missing_word(i, GLOBAL_DICT)
                            if check_two is None:
                                check_three = extra_word(i, GLOBAL_DICT)
                                if check_three is None:
                                    unknown_words.append(current_word)
                                    corrected_words.append(current_word)
                                else:
                                    check_three = replace_case(check_three, case_data[1])
                                    check_three = replace_punc(check_three, current_word, punc_data[1], punc_data[2])
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
        elif i[1] in GLOBAL_DICT[i[0]]:
            if i in GLOBAL_DICT[i[0]][i[1]]:
                corrected_words.append(i)
            else:
                punc_data = punctuation_init(i)
                i = punc_data[0]
                if i[1] in GLOBAL_DICT[i[0]]:
                    if i in GLOBAL_DICT[i[0]][i[1]]:
                        i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                        corrected_words.append(i)
                    else:
                        if i[0] == i[0].upper():
                            case_data = i, True
                            if i[1] in GLOBAL_DICT[i[0]]:
                                temp = i.lower()
                                if i in GLOBAL_DICT[i[0]][i[1]]:
                                    i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                                    corrected_words.append(i)
                                elif temp[1] in GLOBAL_DICT[temp[0]]:
                                    if temp in GLOBAL_DICT[temp[0]][temp[1]]:
                                        i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                                        corrected_words.append(i)
                                    else:
                                        check = adjacent_error(i, GLOBAL_DICT)
                                        if check is None:
                                            check_two = missing_word(i, GLOBAL_DICT)
                                            if check_two is None:
                                                check_three = extra_word(i, GLOBAL_DICT)
                                                if check_three is None:
                                                    check = adjacent_error(temp, GLOBAL_DICT)
                                                    if check is None:
                                                        check_two = missing_word(temp, GLOBAL_DICT)
                                                        if check_two is None:
                                                            check_three = extra_word(temp, GLOBAL_DICT)
                                                            if check_three is None:
                                                                unknown_words.append(current_word)
                                                                corrected_words.append(current_word)
                                                            else:
                                                                check_three = replace_case(check_three, case_data[1])
                                                                check_three = replace_punc(check_three, current_word, \
                                                                                           punc_data[1], punc_data[2])
                                                                mispelled_words.append(current_word)
                                                                corrected_words.append(check_three)
                                                        else:
                                                            check_two = replace_case(check_two, case_data[1])
                                                            check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                                     punc_data[2])
                                                            mispelled_words.append(current_word)
                                                            corrected_words.append(check_two)
                                                    else:
                                                        check = replace_case(check, case_data[1])
                                                        check = replace_punc(check, current_word, punc_data[1],
                                                                             punc_data[2])
                                                        mispelled_words.append(current_word)
                                                        corrected_words.append(check)
                                                else:
                                                    check_three = replace_case(check_three, case_data[1])
                                                    check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                               punc_data[2])
                                                    mispelled_words.append(current_word)
                                                    corrected_words.append(check_three)
                                            else:
                                                check_two = replace_case(check_two, case_data[1])
                                                check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                         punc_data[2])
                                                mispelled_words.append(current_word)
                                                corrected_words.append(check_two)
                                        else:
                                            check = replace_case(check, case_data[1])
                                            check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check)
                                else:
                                    check = adjacent_error(i, GLOBAL_DICT)
                                    if check is None:
                                        check_two = missing_word(i, GLOBAL_DICT)
                                        if check_two is None:
                                            check_three = extra_word(i, GLOBAL_DICT)
                                            if check_three is None:
                                                check = adjacent_error(temp, GLOBAL_DICT)
                                                if check is None:
                                                    check_two = missing_word(temp, GLOBAL_DICT)
                                                    if check_two is None:
                                                        check_three = extra_word(temp, GLOBAL_DICT)
                                                        if check_three is None:
                                                            unknown_words.append(current_word)
                                                            corrected_words.append(current_word)
                                                        else:
                                                            check_three = replace_case(check_three, case_data[1])
                                                            check_three = replace_punc(check_three, current_word, \
                                                                                       punc_data[1], punc_data[2])
                                                            mispelled_words.append(current_word)
                                                            corrected_words.append(check_three)
                                                    else:
                                                        check_two = replace_case(check_two, case_data[1])
                                                        check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                                 punc_data[2])
                                                        mispelled_words.append(current_word)
                                                        corrected_words.append(check_two)
                                                else:
                                                    check = replace_case(check, case_data[1])
                                                    check = replace_punc(check, current_word, punc_data[1],
                                                                         punc_data[2])
                                                    mispelled_words.append(current_word)
                                                    corrected_words.append(check)
                                            else:
                                                check_three = replace_case(check_three, case_data[1])
                                                check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                           punc_data[2])
                                                mispelled_words.append(current_word)
                                                corrected_words.append(check_three)
                                        else:
                                            check_two = replace_case(check_two, case_data[1])
                                            check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                     punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_two)
                                    else:
                                        check = replace_case(check, case_data[1])
                                        check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check)
                        else:
                            case_data = find_case(i)
                            i = case_data[0]
                            if i[1] in GLOBAL_DICT[i[0]]:
                                if i in GLOBAL_DICT[i[0]][i[1]]:
                                    i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                                    corrected_words.append(i)
                                else:
                                    check = adjacent_error(i, GLOBAL_DICT)
                                    if check is None:
                                        check_two = missing_word(i, GLOBAL_DICT)
                                        if check_two is None:
                                            check_three = extra_word(i, GLOBAL_DICT)
                                            if check_three is None:
                                                unknown_words.append(current_word)
                                                corrected_words.append(current_word)
                                            else:
                                                check_three = replace_case(check_three, case_data[1])
                                                check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                           punc_data[2])
                                                mispelled_words.append(current_word)
                                                corrected_words.append(check_three)
                                        else:
                                            check_two = replace_case(check_two, case_data[1])
                                            check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                     punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_two)
                                    else:
                                        check = replace_case(check, case_data[1])
                                        check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check)
        else:
            punc_data = punctuation_init(i)
            i = punc_data[0]
            if i[1] in GLOBAL_DICT[i[0]]:
                if i in GLOBAL_DICT[i[0]][i[1]]:
                    i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                    corrected_words.append(i)
                else:
                    if i[0] == i[0].upper():
                        case_data = i, False
                        if i[1] in GLOBAL_DICT[i[0]]:
                            temp = i.lower()
                            if i in GLOBAL_DICT[i[0]][i[1]]:
                                i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                                corrected_words.append(i)
                            elif temp in GLOBAL_DICT[temp[0]][temp[1]]:
                                i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                                corrected_words.append(i)
                            else:
                                check = adjacent_error(i, GLOBAL_DICT)
                                if check is None:
                                    check_two = missing_word(i, GLOBAL_DICT)
                                    if check_two is None:
                                        check_three = extra_word(i, GLOBAL_DICT)
                                        if check_three is None:
                                            unknown_words.append(current_word)
                                            corrected_words.append(current_word)
                                        else:
                                            check_three = replace_case(check_three, case_data[1])
                                            check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                       punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_three)
                                    else:
                                        check_two = replace_case(check_two, case_data[1])
                                        check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                 punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_two)
                                else:
                                    check = replace_case(check, case_data[1])
                                    check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check)
                    else:
                        case_data = find_case(i)
                        i = case_data[0]
                        if i[1] in GLOBAL_DICT[i[0]]:
                            if i in GLOBAL_DICT[i[0]][i[1]]:
                                i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                                corrected_words.append(i)
                            else:
                                check = adjacent_error(i, GLOBAL_DICT)
                                if check is None:
                                    check_two = missing_word(i, GLOBAL_DICT)
                                    if check_two is None:
                                        check_three = extra_word(i, GLOBAL_DICT)
                                        if check_three is None:
                                            unknown_words.append(current_word)
                                            corrected_words.append(current_word)
                                        else:
                                            check_three = replace_case(check_three, case_data[1])
                                            check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                       punc_data[2])
                                            mispelled_words.append(current_word)
                                            corrected_words.append(check_three)
                                    else:
                                        check_two = replace_case(check_two, case_data[1])
                                        check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                                 punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_two)
                                else:
                                    check = replace_case(check, case_data[1])
                                    check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check)
            else:
                if i[0] == i[0].upper():
                    case_data = i, False
                    if i[1] in GLOBAL_DICT[i[0]]:
                        temp = i.lower()
                        if i in GLOBAL_DICT[i[0]][i[1]]:
                            i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                            corrected_words.append(i)
                        elif temp in GLOBAL_DICT[temp[0]][temp[1]]:
                            i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                            corrected_words.append(i)
                        else:
                            check = adjacent_error(i, GLOBAL_DICT)
                            if check is None:
                                check_two = missing_word(i, GLOBAL_DICT)
                                if check_two is None:
                                    check_three = extra_word(i, GLOBAL_DICT)
                                    if check_three is None:
                                        unknown_words.append(current_word)
                                        corrected_words.append(current_word)
                                    else:
                                        check_three = replace_case(check_three, case_data[1])
                                        check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                   punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_three)
                                else:
                                    check_two = replace_case(check_two, case_data[1])
                                    check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                             punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check_two)
                            else:
                                check = replace_case(check, case_data[1])
                                check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check)
                else:
                    case_data = find_case(i)
                    i = case_data[0]
                    if i[1] in GLOBAL_DICT[i[0]]:
                        if i in GLOBAL_DICT[i[0]][i[1]]:
                            i = replace_punc(i, current_word, punc_data[1], punc_data[2])
                            corrected_words.append(i)
                        else:
                            check = adjacent_error(i, GLOBAL_DICT)
                            if check is None:
                                check_two = missing_word(i, GLOBAL_DICT)
                                if check_two is None:
                                    check_three = extra_word(i, GLOBAL_DICT)
                                    if check_three is None:
                                        unknown_words.append(current_word)
                                        corrected_words.append(current_word)
                                    else:
                                        check_three = replace_case(check_three, case_data[1])
                                        check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                                   punc_data[2])
                                        mispelled_words.append(current_word)
                                        corrected_words.append(check_three)
                                else:
                                    check_two = replace_case(check_two, case_data[1])
                                    check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                             punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check_two)
                            else:
                                check = replace_case(check, case_data[1])
                                check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check)
                    else:
                        check = adjacent_error(i, GLOBAL_DICT)
                        if check is None:
                            check_two = missing_word(i, GLOBAL_DICT)
                            if check_two is None:
                                check_three = extra_word(i, GLOBAL_DICT)
                                if check_three is None:
                                    unknown_words.append(current_word)
                                    corrected_words.append(current_word)
                                else:
                                    check_three = replace_case(check_three, case_data[1])
                                    check_three = replace_punc(check_three, current_word, punc_data[1], \
                                                               punc_data[2])
                                    mispelled_words.append(current_word)
                                    corrected_words.append(check_three)
                            else:
                                check_two = replace_case(check_two, case_data[1])
                                check_two = replace_punc(check_two, current_word, punc_data[1], \
                                                         punc_data[2])
                                mispelled_words.append(current_word)
                                corrected_words.append(check_two)
                        else:
                            check = replace_case(check, case_data[1])
                            check = replace_punc(check, current_word, punc_data[1], punc_data[2])
                            mispelled_words.append(current_word)
                            corrected_words.append(check)
    return mispelled_words, unknown_words, word_tally, corrected_words

