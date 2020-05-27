#################################################
# hw1.py
#
# Your name:
# Your andrew id:
# Collaborator andrew ids:
#################################################

import cs112_m20_week1_linter
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

def isEquilateralTriangle(side1,side2,side3):
    return 42

def isPerfectSquare(n):
    return 42

#################################################
# Test Functions
#################################################

def testIsEquilateralTriangle():
    print('Testing isEquilateralTriangle()... ', end='')
    assert(isEquilateralTriangle(1,2,3) == False)
    assert(isEquilateralTriangle(1,2.0,3) == False)
    assert(isEquilateralTriangle(1.00000000000000001,1.0,1) == True)
    assert(isEquilateralTriangle(.1 + .1 + .1,.3,.3) == True)
    assert(isEquilateralTriangle(11,11,11) == True)
    assert(isEquilateralTriangle(1,1,3) == False)
    assert(isEquilateralTriangle(1,3,3) == False)
    assert(isEquilateralTriangle(1,3,1) == False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testIsEquilateralTriangle()
    testIsPerfectSquare()

def main():
    cs112_m20_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
