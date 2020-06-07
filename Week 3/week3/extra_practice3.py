#################################################
# extra_practice3.py
#################################################

import cs112_f19_week3_linter
import math
from tkinter import *
import string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
################################################

def vowelCount(s):
    vowel = "aeiou"
    i = 0
    count = 0
    while (i < len(s)):
        if (s[i] in vowel or s[i] in vowel.upper()):
            count += 1
        i += 1
    return count

def interleave(s1, s2):
    length = max(len(s1), len(s2))
    output = ""
    i = 0
    while (i < length):
        if (i < len(s1)):
            output = output + s1[i]
        if (i < len(s2)):
            output = output + s2[i]    
        i += 1
    return output

def longestCommonSubstring(s1, s2):
    longest = ""
    i = 0
    while (i < len(s1)):
        j = 0
        while (j < len(s2)):
            if (s1[i] == s2[j]):
                k = 0
                common = "" 
                while (i + k < len(s1) and j + k < len(s2)):
                    if (s1[i + k] == s2[j + k]):
                        common = common + s1[i + k]
                        if (len(longest) < len(common)):
                            longest = common
                        elif (len(longest) == len(common)):
                            longest = min(longest, common)
                        k += 1                        
                        # print(k)
                    else:
                        break
            j += 1
            # print(j)
        i += 1
        # print(i)

    return longest
def countOcc(s, letter):
    i = 0 
    count = 0
    while (i < len(s)):
        if (s[i] == letter):
            count += 1
        i += 1
    return count


def leastFrequentLetters(s):
    s = s.lower()
    leastFreq = ""
    least = 0
    for i in string.ascii_lowercase:
        if (i in s):
            count = countOcc(s, i)
            if (count < least or least == 0):
                least = count 
                leastFreq = i
            elif (count == least):
                leastFreq = leastFreq + i
            else:
                continue
    return leastFreq

def sameChars(s1, s2):
    if (type(s1) == str and type(s2) == str):
        for i in s1:
            if (i not in s2):
                return False
        for j in s2:
            if (j not in s1):
                return False
    else:
        return False

    return True

def areAnagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if (len(s1) == len(s2)):
        for i in s1:
            if (s1.count(i) != s2.count(i)):
                return False
    else:
        return False        

    return True

def replace(s1, s2, s3):
    i = 0
    while (i < len(s1)):
        j = 0
        while (j < len(s2)):
            if (s1[i] == s2[j]):
                i += 1
                j += 1
            else:
                break
        if (j != 0):
            s1 = s1[:(i - j)] + s3 + s1[i:]
        i += 1
        # print(i)
    return s1

def wordWrap(text, width):
    output = """"""
    i = 0
    while (i < len(text)):
        if (i >= width and i % width == 0):
            output = output + "\n"
            output = output + text[i:(i + width)].strip()
            output = output.replace(" ", "-")
        else:
            output = output + text[i:(i + width)].strip()
            output = output.replace(" ", "-")
        i += width

    return output

#################################################
# Test Functions
#################################################

def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert(leastFrequentLetters("") == "")
    assert(leastFrequentLetters(string.punctuation) == "")
    assert(leastFrequentLetters(string.whitespace) == "")
    assert(leastFrequentLetters(string.ascii_lowercase) ==
                                string.ascii_lowercase)
    assert(leastFrequentLetters(string.ascii_uppercase) ==
                                string.ascii_lowercase)
    noq = string.ascii_lowercase.replace('q','')
    nor = string.ascii_lowercase.replace('r','')
    nos = string.ascii_lowercase.replace('s','')
    assert(leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    assert(leastFrequentLetters(nor + string.ascii_lowercase) == "r")
    assert(leastFrequentLetters(nos + nor + " aaa " + 5*string.ascii_lowercase)
                                == "rs")
    print("Passed!")

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("abcabcabc", "cba") == True)
    assert(sameChars("abcabcabc", "cbad") == False)
    assert(sameChars("abcabcabc", "cBa") == False)
    assert(sameChars(42,"The other parameter is not a string") == False)
    assert(sameChars("","") == True)
    print("Passed!")

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

def testReplace():
    print('Testing replace()...', end='')
    assert(replace('abc', 'd', 'e') == 'abc'.replace('d', 'e'))
    assert(replace('abc', 'b', 'e') == 'abc'.replace('b', 'e'))
    assert(replace('abcb abc', 'b', 'e') == 'abcb abc'.replace('b', 'e'))
    assert(replace('abcb abc', 'ab', 'abd') == 'abcb abc'.replace('ab', 'abd'))
    print('Passed!')

def testWordWrap():
    print('Testing wordWrap()...', end='')
    assert(wordWrap("abc", 3) == "abc")
    assert(wordWrap("abc",2) == "ab\nc") 
    assert(wordWrap("abcdefghij", 4)  ==  """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg",  4)  ==  """\
a-b
c-de
fg""")
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testVowelCount()
    testInterleave()
    testLongestCommonSubstring()
    testLeastFrequentLetters()
    testSameChars()
    testAreAnagrams()
    testReplace()
    testWordWrap()

def main():
    cs112_f19_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
