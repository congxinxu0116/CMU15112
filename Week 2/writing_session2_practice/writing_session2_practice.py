#################################################
# writing_session2_practice.py
#################################################

import cs112_f19_week2_linter
import math
from tkinter import *

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

def IsPrime(n):
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

def nthPrime (n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (IsPrime(guess)):
            found += 1
    return guess
#################################################
# Functions for you to write
#################################################

def digitCount(n):
    #if (abs(n) < 10):
    #    return 1
    #else:
    #    digit = 2
    #    result = 66
    #    while (result > 0):
    #        result = abs(n) // 10 ** digit            
    #        digit += 1            
    #    return digit - 1
    if (n == 0): return 1
    n = abs(n)
    count = 0
    while (n > 0) :
        count += 1
        n //= 10
    return count

def gcd(a,b):
    #c = 1
    #while (c != 0):
    #    c = a % b
    #    a = b
    #    b = c
    #return(a) 
    while(b > 0):
        a,b = b, a % b
    return a

def hasConsecutiveDigits(n):
    n = abs(n)
    digit0 = -1
    while (n > 0):     
        digit1 = n % 10 
        if (digit0 == digit1):
            return True
        n //= 10
        digit0 = digit1
    return False

    # if (abs(n) < 10):
    #     return False
    # else:
    #     digit = 2
    #     result = 0
    #     while (result != abs(n)):
    #         result = abs(n) % 10 ** digit
    #         print(result) 
    #         while (result > 99):
    #             result = result // 10
    #             print(result)

    #         if (result % 10 == 0 
    #             or result // 10 == result % 10):
    #             return True

    #         if (digitCount(n) > digit): 
    #             digit += 1 
    #         else:             
    #             return False
def countOcc(n, number):
    if (n == 0 and number == 0):
        return 1
    count = 0   
    while (n > 0):          
        digit1 = n % 10 
        if (number == digit1):
            count += 1
        n //= 10        
    return count

def mostFrequentDigit(n):
    count_max = -1    
    for i in range(0, 9 + 1):        
        count_i = countOcc(n, i)
        if (count_i > count_max):
            count_max = count_i
            result = i
    return result

def nthAdditivePrime(n):
    found = 0
    guess = 0
    
    while (found <= n):
        guess += 1
        if (IsPrime(guess)):
            number = guess
            sumdigit = 0
            while (number > 0):
                newdigit = number % 10
                sumdigit = sumdigit + newdigit
                number //= 10
            if (IsPrime(sumdigit)):
                found += 1
    return guess

def nthPalindromicPrime(n):
    return 42

def isRotation(x, y):
    return 42

def findZeroWithBisection(f, x0, x1, epsilon):
    return 42

def carrylessAdd(x1, x2):
    return 42

def drawDashedLine(dashLength, canvas, width, height):
    pass

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed.')

def testGcd():
    print('Testing gcd()...', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed.')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed.')

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed.')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed.')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def runDrawDashedLine(dashLength, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawDashedLine(dashLength, canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawDashedLine():
    print('Calling runDrawDashedLine(5, 400, 400):')
    runDrawDashedLine(5, 400, 400)
    print('Calling runDrawDashedLine(20, 800, 400):')
    runDrawDashedLine(20, 800, 400)

#################################################
# testAll and main
#################################################

def testAll():
    testDigitCount()
    testGcd()   
    testHasConsecutiveDigits()   
    testMostFrequentDigit()
    testNthAdditivePrime()   
    testNthPalindromicPrime()
    testIsRotation()
    testFindZeroWithBisection()
    testCarrylessAdd()
    testDrawDashedLine()

def main():
    cs112_f19_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
