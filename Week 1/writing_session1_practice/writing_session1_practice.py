#################################################
# writing_session1_practice.py
# http://www.kosbie.net/cmu/fall-19/15-112/notes/writing-session1.html
# Your name: Congxin Xu
# Your andrew id: xu1214
#################################################

import cs112_f19_week1_linter
import math

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
# Write the function distance(x1, y1, x2, y2) that takes 
# four int or float values x1, y1, x2, y2 that represent 
# the two points (x1, y1) and (x2, y2), and returns the
# distance between those points as a float.
def distance(x1, y1, x2, y2):
    dis_x = abs(x1 - x2)
    dis_y = abs(y1 - y2)
    output = math.sqrt(dis_x**2 + dis_y**2)
    return output

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    dis_x = abs(x1 - x2)
    dis_y = abs(y1 - y2)
    if (r1 + r2 < math.sqrt(dis_x**2 + dis_y**2)):
        return False
    return True

def getInRange(x, bound1, bound2):
    if ((x <= bound1 and x >= bound2) or 
        (x >= bound1 and x <= bound2)):
        return x
    if (x == min(x, bound1, bound2)):
        return min(bound1, bound2)
    if (x == max(x, bound1, bound2)):
        return max(bound1, bound2)

def eggCartons(eggs):
    if (eggs == 0):
        carton = 0
    else:
        mod = eggs % 12        
        if (mod == 0):
            carton = eggs / 12
        else:
            carton = (eggs // 12) + 1 
    return carton

def pascalsTriangleValue(row, col):
    if (col <= row and row >= 0 and col >= 0):
        nom = math.factorial(row)
        denom = math.factorial(col) * math.factorial(row - col)  
        return nom / denom

def isFactor(f, n):
    if (n == 0):
        return True
    elif (f == 0):
        return False
    elif (n % f == 0):
        return True
    else:
        return False

def isMultiple(m, n):
    if (m == 0):
        return True
    elif (n == 0):
        return False
    elif (m % n == 0):
        return True
    else:
        return False

def nearestBusStop(street):
    if (street == 0):
        return 0
    elif (street % 8 <= 4):
        return (street // 8) * 8
    else:    
        return ((street // 8) + 1)* 8

def getKthDigit(n, k):   
    if (abs(n) > 10**k):
        return (abs(n) // (10**k)) % 10
    else:
        return 0

def setKthDigit(n, k, d):
    x = getKthDigit(n, k)
    if (abs(n) > 10**k):
        if (n > 0):
            return n - (10**k)*x + (10**k)*d
        else:
            return n + (10**k)*x - (10**k)*d      
    else:
        if (n >= 0):
            return n + (10**k)*d
        else:
            return n - (10**k)*d
        

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed.')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed.')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed.')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed.')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed.')

def testIsFactor():
    print('Testing isFactor()... ', end='')
    assert(isFactor(1,1) == True)
    assert(isFactor(2,10) == True)
    assert(isFactor(-5,25) == True)
    assert(isFactor(5,0) == True)
    assert(isFactor(0,0) == True)
    assert(isFactor(2,11) == False)
    assert(isFactor(10,2) == False)
    assert(isFactor(0,5) == False)
    print('Passed.')

def testIsMultiple():
    print('Testing isMultiple()... ', end='')
    assert(isMultiple(1,1) == True)
    assert(isMultiple(2,10) == False)
    assert(isMultiple(-5,25) == False)
    assert(isMultiple(5,0) == False)
    assert(isMultiple(0,0) == True)
    assert(isMultiple(2,11) == False)
    assert(isMultiple(10,2) == True)
    assert(isMultiple(0,5) == True)
    assert(isMultiple(25,-5) == True)
    print('Passed.')

def testNearestBusStop():
    print('Testing nearestBusStop()... ', end='')
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-1, 4, 7) == -70001)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testIsFactor()
    testIsMultiple()
    testNearestBusStop()
    testGetKthDigit()
    testSetKthDigit()

def main():
    cs112_f19_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
