#################################################
# writing_session3_practice_solutions.py
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
#################################################

def rotateString(s, k):
    if (k > 0):
        for i in range(1, k + 1):
            s = s[1:len(s)] + s[0]
        return s
    else:
        k = abs(k)
        for i in range(1, k + 1):
            s = s[len(s) - 1] + s[:len(s) - 1]
        return s

def applyCaesarCipher(message, shift):
    output = ""
    for i in message:
        if (i in string.ascii_lowercase):
            x = (ord(i) + shift - ord('a')) % 26
            x = chr(x + ord('a'))
        elif (i in string.ascii_uppercase):
            x = (ord(i) + shift - ord('A')) % 26
            x = chr(x + ord('A'))
        else:
            x = i        
        output = output + x
    return output


def hasBalancedParentheses(s):
    right = 0
    for i in s:
        if (ord(i) == ord('(')):
            right += 1            
        elif (ord(i) == ord(')')):
            if (right > 0):
                right -= 1
            else:
                return False
        else:
            continue    
    if (right == 0):
        return True
    else:
        return False

def largestNumber(s):
    i = 0 # total index for s
    j = 0 # index for digits
    k = 0 # index for non-digits
    number = ""
    largest = 0
    while (i < len(s)):
        if (s[i] in string.digits):
            j = i
            while (j < len(s)):
                number = number + s[j] 
                if (j + 1 >= len(s) 
                    or s[j + 1] not in string.digits):
                    largest = max(largest, int(number))
                    number = ""
                    break
                else:
                    j += 1
        else:
            k += 1
        i += 1
    if (k != len(s)):
        return largest

def getOrder(s):
    total = 0
    for i in s:
        total = total + ord(i)
    return total


def longestSubpalindrome(s):
    i = 0
    pal = ""
    longest = ""
    while (i + 1 < len(s)):
        if (s[i - 1] == s[i + 1]):
            j = 1
            while (i + j < len(s) and i - j >= 0):
                if (s[i - j] == s[i + j]):
                    pal = s[(i - j):(i + j + 1)]
                    if (getOrder(longest) < getOrder(pal)):
                        longest = pal
                    j += 1
                    print(j)
                else:
                    break
            i += 1
        else:
            i += 1 
    
    if (len(s) == 1):
        return s
    else:
        return longest

def collapseWhitespace(s):
    i = 0
    output = ""
    while (i < len(s)):
        if (s[i].isspace()):
            j = 0
            while(i + j < len(s)):
                if (s[i + j].isspace()):
                    j += 1
                else:
                    break
            output = output + " "
            i = i + j
        else: 
            output = output + s[i]
            i += 1

    return output

def topScorer(data):    
    topscore = 0
    name = ""
    if (data != ""):
        for line in data.splitlines():
            # print(line)
            person = line.split(",")
            i = 1
            score = 0

            while (i < len(person)):
                score = score + int(person[i])
                i += 1

            if (score > topscore):
                topscore = score
                name = person[0]
            elif (score == topscore):
                name = name + "," + person[0]
        
        return name

def drawFlagOfQatar(canvas, width, height):
    canvas.create_text(width/2, height/2, text='<TBD: Draw Flag of Qatar>')

def drawFlagOfTheEU(canvas, width, height):
    canvas.create_text(width/2, height/2, text='<TBD: Draw Flag of the EU>')

#################################################
# Test Functions
#################################################

def testRotateString():
    print("Testing rotateString()...", end="")
    assert(rotateString("abcde", 0) == "abcde")
    assert(rotateString("abcde", 1) == "bcdea")
    assert(rotateString("abcde", 2) == "cdeab")
    assert(rotateString("abcde", 3) == "deabc")
    assert(rotateString("abcde", 4) == "eabcd")
    assert(rotateString("abcde", 5) == "abcde")
    assert(rotateString("abcde", 25) == "abcde")
    assert(rotateString("abcde", 28) == "deabc")
    assert(rotateString("abcde", -1) == "eabcd")
    assert(rotateString("abcde", -2) == "deabc")
    assert(rotateString("abcde", -3) == "cdeab")
    assert(rotateString("abcde", -4) == "bcdea")
    assert(rotateString("abcde", -5) == "abcde")
    assert(rotateString("abcde", -25) == "abcde")
    assert(rotateString("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
                             "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
                             "zabcdefghijklmnopqrstuvwxy")
    assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed.")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False) 
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def runDrawFlagOfQatar(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawFlagOfQatar(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawFlagOfQatar():
    print('Calling runDrawFlagOfQatar(400, 400):')
    runDrawFlagOfQatar(400, 400)
    print('Calling runDrawFlagOfQatar(800, 400):')
    runDrawFlagOfQatar(800, 400)

def runDrawFlagOfTheEU(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawFlagOfTheEU(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawFlagOfTheEU():
    print('Calling runDrawFlagOfTheEU(400, 400):')
    runDrawFlagOfTheEU(400, 400)
    print('Calling runDrawFlagOfTheEU(800, 400):')
    runDrawFlagOfTheEU(800, 400)

#################################################
# testAll and main
#################################################

def testAll():
    testRotateString()
    testApplyCaesarCipher()
    testHasBalancedParentheses()
    testLargestNumber()
    testLongestSubpalindrome()
    testCollapseWhitespace()
    testTopScorer()
    # testDrawFlagOfQatar()
    # testDrawFlagOfTheEU()

def main():
    cs112_f19_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
