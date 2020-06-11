#################################################
# writing_session4_practice_solutions.py
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

def alternatingSum(L):
    i = 0
    total = 0
    while (i < len(L)):
        total = total + L[i] * ((-1) ** i)
        i += 1
    return total

def median(L):
    length = len(L)
    L = sorted(L)
    if (length != 0 and length % 2 == 0):
        return (L[int(length / 2)] + 
                L[int(length / 2 - 1)]) / 2
    elif (length % 2 != 0):
        return L[length // 2]


def isSorted(L):
    if len(L) <= 1:
        return True
    else:
        lessThan = 0
        greaterThan = 0
        i = 0
        while i + 1 < len(L):
            if L[i] < L[i + 1]:
                lessThan += 1
            elif L[i] > L[i + 1]:
                greaterThan += 1
            else:
                lessThan += 1
                greaterThan += 1
            i += 1
        if (lessThan == len(L) - 1 or
            greaterThan == len(L) - 1):
            return True
        else:
            return False

def smallestDifference(L):
    if len(L) == 0:
        return -1
    elif len(L) == 1:
        return 0
    else: 
        L = sorted(L)
        i = 0
        diff = 0
        while (i + 1 < len(L)):
            tmp = abs(L[i] - L[i + 1])
            if (i == 0):
                diff = tmp
            elif (tmp < diff):
                diff = tmp            
            i += 1
        return diff 


def lookAndSay(L):
    if (len(L) == 0):
        return []
    else:
        i = 0
        output = []
        while (i < len(L)):
            j = i + 1
            count = 1
            while (j < len(L)):
                if (L[i] == L[j]):
                    count += 1
                    j += 1
                else:
                    break
            output = output + [(count,L[i])]
            i = j
    return output

def inverseLookAndSay(L):
    output = []
    for i in L:
        output = output + [i[1]] * i[0]
    return output

def multiplyPolynomials(p1, p2):
    output = []    
    for k in range(0, len(p1) + len(p2) - 1):
        final = 0
        i = 0
        while (i < len(p1)):
            j = 0
            while (j < len(p2)):
                if (i + j == k):
                    tmp = p1[i] * p2[j]
                    final = final + tmp
                j += 1
            i += 1
        output = output + [final]
    return output

def nondestructiveRemoveRepeats(L):
    newL = []
    for i in L:
        if (i not in newL):
            newL = newL + [i]
    return newL

def destructiveRemoveRepeats(L):
    i = 0
    while (i < len(L)):
        j = i + 1
        while (j < len(L)):
            if (L[i] == L[j]):
                L.pop(j)
            else:
                j += 1
        i += 1
    

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed.')

def testMedian():
    print('Testing median()...', end='')
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed')

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed')

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()
    testMedian()
    testIsSorted()
    testSmallestDifference()
    testLookAndSay()
    testInverseLookAndSay()
    testMultiplyPolynomials()    
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()

def main():
    cs112_f19_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
