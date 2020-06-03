#################################################
# hw2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week2_linter
import math
from tkinter import *
import random

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

def getnumber(n, i):
    # n is the number
    # i is the i-th digit
    # getnumber(3528, 3) = 5
    
    if (i <= digitCount(n)):
        return n // 10 ** (i - 1) % 10

def fasterIsPrime(n):
    if (n < 2):
        return False 
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n ** 0.5)
    for factor in range(3, maxFactor + 1, 2):
        if (n % factor == 0):
            return False
    return True

def digitCount(n):
    n = abs(n)
    # count the number of digits in n
    i = 0 # Count record
    x = 1 # Integer dividion check
    while (x > 0):
        x = n // 10
        n //= 10
        i += 1
    return i
#################################################
# Functions for you to write
#################################################

def integral(f, a, b, N):
    deltax = (b - a) / N
    tmp = 0 
    for i in range(1, N):
        tmp = tmp + f(a + i * deltax)    
    return deltax * (tmp + (f(b) + f(a)) / 2)

def isFactor(n, x):
    if (n % x == 0):
        return True
    else:
        return False

def isSmithNumber(n):

    if (not fasterIsPrime(n)):
        sumofdigits = 0 
        # Calculate Sum of Digits
        i = 1
        while (i <= digitCount(n)):
            sumofdigits = sumofdigits + getnumber(n, i)
            i += 1
        
        # Calculate sum of digits of the prime factors
        j = 1
        k = 1
        sumofprimedigits = 0
        while (j <= n):
            if (fasterIsPrime(j) and isFactor(n, j)):
                while (k <= digitCount(j)):
                    sumofprimedigits = sumofprimedigits + getnumber(j, k)
                    k += 1
                n = n // j
                j = 1
                k = 1
            else:
                j += 1
        # print(sumofdigits)
        # print(sumofprimedigits)
        if (sumofdigits == sumofprimedigits):
            return True
        else:
            return False
    else: 
        return False


def nthSmithNumber(n):
    found = 0 
    guess = 1
    while (found <= n): 
        if (isSmithNumber(guess)):
            found += 1
        guess += 1 
    return guess - 1       

def drawPattern1(points, canvas, width, height):
    pass

def drawPattern2(points, canvas, width, height):
    pass

def drawPattern3(points, canvas, width, height):
    pass

def drawPattern4(canvas, width, height):
    pass

def playPig():
    print('Not yet implemented!')

#################################################
# Bonus/Optional functions for you to write
#################################################

def bonusCarrylessMultiply(x1, x2):
    return 42

def bonusPlay112(game):
    return 42

#################################################
# Test Functions
#################################################

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def runDrawPattern1(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern1(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern2(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern2(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern3(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern3(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern4(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern4(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawPatterns():
    print('** Note: You need to manually test drawPatterns()')
    print('Calling runDrawPattern1(5, 400, 400):')
    runDrawPattern1(5, 400, 400)
    print('Calling runDrawPattern1(10, 800, 400):')
    runDrawPattern1(10, 800, 400)
    print('Calling runDrawPattern2(5, 400, 400):')
    runDrawPattern2(5, 400, 400)
    print('runDrawPattern2(10, 800, 400):')
    runDrawPattern2(10, 800, 400)
    print('runDrawPattern3(5, 400, 400):')
    runDrawPattern3(5, 400, 400)
    print('runDrawPattern3(10, 800, 400)')
    runDrawPattern3(10, 800, 400)
    print('runDrawPattern4(600, 600)')
    runDrawPattern4(600, 600)

def testPlayPig():
    print('** Note: You need to manually test playPig()')

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testBonusPlay112():
    print("Testing bonusPlay112()... ", end="")
    assert(bonusPlay112( 5 ) == "88888: Unfinished!")
    assert(bonusPlay112( 521 ) == "81888: Unfinished!")
    assert(bonusPlay112( 52112 ) == "21888: Unfinished!")
    assert(bonusPlay112( 5211231 ) == "21188: Unfinished!")
    assert(bonusPlay112( 521123142 ) == "21128: Player 2 wins!")
    assert(bonusPlay112( 521123151 ) == "21181: Unfinished!")
    assert(bonusPlay112( 52112315142 ) == "21121: Player 1 wins!")
    assert(bonusPlay112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(bonusPlay112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(bonusPlay112( 51211 ) == "28888: Player 2: occupied!")
    assert(bonusPlay112( 5122221 ) == "22888: Player 1: occupied!")
    assert(bonusPlay112( 51261 ) == "28888: Player 2: offboard!")
    assert(bonusPlay112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testIntegral()
    testNthSmithNumber()
    testDrawPatterns()
    testPlayPig()
    #testBonusCarrylessMultiply()
    #testBonusPlay112()

def main():
    cs112_f19_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
