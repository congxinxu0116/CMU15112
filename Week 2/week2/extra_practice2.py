#################################################
# extra_practice2.py
#
# Your name:
# Your andrew id:
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

def getnumber(n, i):
    # n is the number
    # i is the i-th digit
    # getnumber(3528, 3) = 5
    
    if (i <= digitCount(n)):
        return n // 10 ** (i - 1) % 10


#################################################
# Functions for you to write
################################################

def longestDigitRun(n):
    n = abs(n)
    if (n < 10):
        return n
    # Find Consecutive
    # Find Length
    # Compare length
    # Compare number
    i = 0
    found = 0    
    length = 1
    newlength = 1
    result = 10
    while (i <= digitCount(n)-2):
        digit0 = getnumber(n, i + 1)
        nextdigit = getnumber(n, i + 2)
        if (digit0 == nextdigit):
            found = digit0
            newlength += 1
            if (length <= newlength):
                length = newlength
                # newlength = 1
                # print(length)
                if (found < result):
                    result = found
                    # print(result)
        else: 
            newlength = 1
        i += 1
    return result       

def isProperty309(n):
    n = n**5
    check = 0
    for x in range(0, 9 + 1):
        i = 1
        while (i <= digitCount(n)):
            if (x != getnumber(n, i)):
                i += 1
            else:
                check += 1 
                break 
        # print("Digit", x, "found.")
    if (check == 10):
        return True
    else:
        # print(check)
        return False
    

def nthWithProperty309(n):
    found = 0 
    guess = 0
    while (found <= n): 
        if (isProperty309(guess)):
            found += 1
        guess += 1 
    return guess - 1

def nthKaprekarNumber(n):
    return 42

def nearestKaprekarNumber(n):
    return 42

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


def isLeftTruncatablePrime(n):
    if (fasterIsPrime(n)):
        check = 0
        for i in range(1, digitCount(n)):
            if (fasterIsPrime(n % 10**i)):
                check += 1
        
        if (check == digitCount(n) - 1):
            return True
        else:
            return False
    
    return False

def nthLeftTruncatablePrime(n):
    found = 0 
    guess = 0
    while (found <= n): 
        if (isLeftTruncatablePrime(guess)):
            found += 1
        guess += 1 
    return guess - 1

def isCarol(n):
    k = math.log((n + 2)**(0.5) + 1, 2)
    if (k == roundHalfUp(k)):
        return True
    else: 
        return False

def isCarolPrime(n):
    if (isCarol(n) and fasterIsPrime(n)):
        return True
    else:
        return False

def nthCarolPrime(n):
    found = 0 
    guess = 0
    while (found <= n): 
        if (isCarolPrime(guess)):
            found += 1
        guess += 1
    return guess - 1

def sumOfSquaresOfDigits(n):
    i = 1
    result = 0
    while (i <= digitCount(n)):
        square = getnumber(n,i) ** 2
        result += square
        i+= 1
    
    return result

def isHappyNumber(n):
    output = 0
    while (output != 1 or output != 4):
        output = sumOfSquaresOfDigits(n)
        
        if (output == 1):
            return True
        elif (output == 4):
            return False
        else:
            n = output


def nthHappyNumber(n):
    found = 0 
    guess = 1
    while (found <= n): 
        if (isHappyNumber(guess)):
            found += 1
        guess += 1
    return guess - 1

def isHappyPrime(n):
    return (isHappyNumber(n) and fasterIsPrime(n))

def nthHappyPrime(n):
    found = 0 
    guess = 1
    while (found <= n): 
        if (isHappyPrime(guess)):
            found += 1
        guess += 1
    return guess - 1

def IsPowerfulNumber(n):
    if (n == 1): return True
    a = 1
    b = 1
    while (a < n):
        while (b < n):
            if (((n % a**3 == 0 
                  and n % b**2 == 0
                  and a**3 * b**2 == n) 
                or (n % a**2 == 0 
                  and n % b**3 == 0 
                  and a**2 * b**3 == n))):
                return True
            else:
                b += 1                
        a += 1
        b = 1        
    return False

def nthPowerfulNumber(n):
    found = 0 
    guess = 0
    while (found <= n): 
        if (IsPowerfulNumber(guess)):
            found += 1
        guess += 1
    return guess - 1

def rotate(n):
    return (n % 10) * (10 ** (digitCount(n) - 1)) + (n // 10)

def primeWithNoZero(n):
    if (fasterIsPrime(n)):
        i = 1
        check = 0
        while (i <= digitCount(n)):
            if (getnumber(n, i) == 0):
                return False
            else:
                i += 1
    else:
        return False
    return True

def isCircularPrime(n):
    if (primeWithNoZero(n)):
        check = 0
        i = 0
        while (i <= digitCount(n)):
            if (fasterIsPrime(n)):
                n = rotate(n)
                i += 1
            else:
                return False
    else:
        return False

    return True   

def nthCircularPrime(n):
    found = 0 
    guess = 0
    while (found <= n): 
        if (isCircularPrime(guess)):
            found += 1
        guess += 1
    return guess - 1

#################################################
# Test Functions
#################################################

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed.')

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(5) == 635)
    assert(nthWithProperty309(6) == 662)
    print('Passed.')

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(10) == 53)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(5) == 17)
    print('Passed.')

def testNthCarolPrime():
    print('Testing nthCarolPrime()... ', end='')
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    print('Passed.')

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
    assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
    assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4+9+16 = 29
    print("Passed.")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed.")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed.")

def testIsHappyPrime():
    print("Testing isHappyPrime()...", end="")
    assert(isHappyPrime(1) == False)
    assert(isHappyPrime(2) == False)
    assert(isHappyPrime(3) == False)
    assert(isHappyPrime(7) == True)
    assert(isHappyPrime(10) == False)
    assert(isHappyNumber(13) == True)
    print("Passed.")

def testNthHappyPrime():
    print("Testing nthHappyPrime...", end="")
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(10) == 167)
    assert(nthHappyPrime(20) == 397)
    print("Passed.")

def testNthPowerfulNumber():
    print('Testing nthPowerfulNumber()... ', end='')
    assert(nthPowerfulNumber(0) == 1)
    assert(nthPowerfulNumber(1) == 4)
    assert(nthPowerfulNumber(2) == 8)
    assert(nthPowerfulNumber(3) == 9)
    assert(nthPowerfulNumber(4) == 16)
    assert(nthPowerfulNumber(5) == 25)
    assert(nthPowerfulNumber(10) == 64)
    assert(nthPowerfulNumber(15) == 121)
    assert(nthPowerfulNumber(20) == 196)
    print('Passed.')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(1) == 3)
    assert(nthCircularPrime(2) == 5)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(16) == 199)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testLongestDigitRun()
    testNthWithProperty309()
    # testNthKaprekarNumber()
    # testNearestKaprekarNumber()
    testNthLeftTruncatablePrime()
    # testNthCarolPrime()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyNumber()
    testNthHappyPrime()
    testNthPowerfulNumber()
    testNthCircularPrime()

def main():
    cs112_f19_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
