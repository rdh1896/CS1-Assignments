"""
Author: Russell Harvey <rdh1896@rit.edu>
File: file_compare.py
Assignment: hw05
Language: Python3
Purpose: Compare the lines in two separate text files.
"""

def char_by_char(txt1, txt2):
    """
    Takes two text files as parameters, then compares them line-by-line.
    If the lines are different length, it will add to the 'mismatch_line'
    variable and add to the sum of the character totals for each file. If
    the lines match in length, it will then analyze both lines character by
    character. If characters do not match, the function will report the line
    number and index number to the variable 'unmatched_chr' and will add one to
    the 'unmatch_chr_num' variable. The for loops that contain this process also
    count all the characters in each file and add them to the 'total_chr' variables.
    Before and at the end of the while loop the function reads the next line and then
    strips it so there will be no extra incidental spaces.
    :param txt1: First text file
    :param txt2: Second text file
    :return: None
    """
    t1 = open(txt1)
    t2 = open(txt2)
    num = 1
    total_chr1 = 0
    total_chr2 = 0
    unmatched_chr = ""
    unmatch_chr_num = 0
    mismatch_line = 0
    # Read lines.
    line1 = t1.readline()
    line2 = t2.readline()
    # Strip the lines of spaces.
    line1 = line1.strip()
    line2 = line2.strip()
    while line1 != "" or line2 != "":
        # If the lengths are not equal, add to mismatch_line and total_chr variables
        if len(line1) != len(line2):
            for i in line1:
                total_chr1 += 1
            for i in line2:
                total_chr2 += 1
            unmatched_chr = unmatched_chr + str(num) + ", "
            num += 1
            mismatch_line += 1
        # Otherwise, now analyze character by character
        else:
            chr = 0
            for i in line1:
                x = line2[chr]
                if i != x:
                    unmatched_chr = unmatched_chr + str(num) + ":" + str(chr) + ", "
                    unmatch_chr_num += 1
                    chr += 1
                    total_chr1 += 1
                    total_chr2 += 1
                else:
                    chr += 1
                    total_chr1 += 1
                    total_chr2 += 1
            num += 1
        # Read next line and strip.
        line1 = t1.readline()
        line2 = t2.readline()
        line1 = line1.strip()
        line2 = line2.strip()
        continue
    print("Character by Character:")
    print("Unmatched characters: " + unmatched_chr)
    print("There are " + str(total_chr1) + " characters in " + txt1)
    print("There are " + str(total_chr2) + " characters in " + txt2)
    print("There were " + str(unmatch_chr_num) + " unmatched characters in the files")
    print("There were " + str(mismatch_line) + " of different length")

def main():
    """
    Takes two .txt files as input then runs them through the char_by_chr function and
    compares them.
    :return:
    """
    txt1 = input("Please enter the first .txt file you would like to compare: ")
    txt2 = input("Please enter the second .txt file you would like to compare: ")
    char_by_char(txt1, txt2)

main()

