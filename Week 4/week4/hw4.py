#################################################
# hw4.py
#
# Your name:
# Your andrew id:
#################################################


import cs112_f19_week4_linter
import math, copy

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

#################################################
# bestScrabbleScore
#################################################
def findWord(word, hand):
    handcopy = hand + []
    i = 0
    while (i < len(word)):
        if (word[i] in handcopy):
            j = 0
            while (j < len(handcopy)):
                if (word[i] == handcopy[j]):
                    handcopy.pop(j)
                    break
                else:
                    j += 1
        else:
            return False
        i += 1
    return True

def findWordScore(word, letterScores):
    total = 0
    for i in word:
        wordscore = letterScores[ord(i) - ord('a')]
        total = total + wordscore
    return total

def bestScrabbleScore(dictionary, letterScores, hand):
    i = 0
    best = 0
    bestWord = []
    while (i < len(dictionary)):
        if (findWord(dictionary[i], hand)):
            tmp = findWordScore(dictionary[i], letterScores)
            if (tmp > best):
                best = tmp
                bestWord = [dictionary[i]]
            elif (tmp == best):
                bestWord = bestWord + [dictionary[i]]
        i += 1
    if (len(bestWord) == 1):
        return tuple((bestWord[0], best))
    elif (len(bestWord) > 1):
        return tuple((bestWord, best))

   

#################################################
# Person class
#################################################

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendlist = []

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getFriends(self):
        if (len(self.friendlist) > 0):
            return self.friendlist

    def addFriend(self, friend):      
        if (friend != self):        
            # Ignore existing friends
            if (friend in self.friendlist):
                pass
            else:
                self.friendlist = self.friendlist + [friend]

#################################################
# playMyTextAdventureGame
#################################################

def playMyTextAdventureGame():
    print('Replace this with someting more fun to play!')

#################################################
# bonus: linearRegression
#################################################

def linearRegression(pointsList):
    return 42

#################################################
# bonus: runSimpleProgram
#################################################

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    assert(fred.getFriends() == None)

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == None)

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(fred.getFriends() == None)
    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    barney = Person('barney', 28)
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, barney])
 
    fred.addFriend(barney)  # don't add twice
    fred.addFriend(fred)    # ignore self as a friend
    assert(fred.getFriends() == [wilma, barney])
    print('Passed!')

def testPlayMyTextAdventureGame():
    print('***************************************************')
    print('Testing playMyTextAdventureGame()...')
    print('This requires manual testing, so we will just run the game:')
    print('***************************************************')
    playMyTextAdventureGame()
    print('***************************************************')

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testBonusLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testBonusRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBestScrabbleScore()
    testPersonClass()
    testPlayMyTextAdventureGame()
    testBonusLinearRegression()
    testBonusRunSimpleProgram()

def main():
    cs112_f19_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
