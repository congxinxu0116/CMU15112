#################################################
# extra_practice1.py (due never)
#
# Your name:
# Your andrew id:
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

def distance(x1, y1, x2, y2):
    dis_x = abs(x1 - x2)
    dis_y = abs(y1 - y2)
    output = math.sqrt(dis_x**2 + dis_y**2)
    return output
#################################################
# Functions for you to write
#################################################

def fabricYards(inches):
    if (inches % 36 == 0):
        return inches // 36
    else:
        return inches // 36 + 1
# OR simply return math.ceil(inches / 36)

def fabricExcess(inches):    
    return fabricYards(inches) * 36 - inches

def isEvenPositiveInt(x):
    if (type(x) == int and x > 0 and x % 2 == 0):
        return True
    else:
        return False

def nthFibonacciNumber(n):
    n = n + 1
    x = 5**0.5
    nom = (1 + x)**n - (1 - x)**n
    den = 2**n * x
    return roundHalfUp(nom / den)

def isLegalTriangle(s1,s2,s3):
    if (s1 < 0 or s2 < 0 or s3 < 0):
        return False
    else:
        x = max(s1, s2, s3)
        if (x == s1 and s2 + s3 <= s1):
            return False
        elif (x == s2 and s1 + s3 <= s2):
            return False
        elif (x == s3 and s1 + s2 <= s3):
            return False    
    return True

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    
    a = distance(x1 = x1, y1 = y1, x2 = x2, y2 = y2)
    b = distance(x1 = x2, y1 = y2, x2 = x3, y2 = y3)
    c = distance(x1 = x3, y1 = y3, x2 = x1, y2 = y1)
    
    x = max(a, b, c)
    if (x == a and almostEqual(a**2, b**2 + c**2)):
        return True
    elif (x == b and almostEqual(b**2, a**2 + c**2)):
        return True
    elif (x == c and almostEqual(c**2, b**2 + a**2)):
        return True    
    
    return False

def triangleArea(s1, s2, s3):
    if (isLegalTriangle(s1, s2, s3)):
        s = (s1 + s2 + s3) / 2
        Area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
        return Area
    return 0

def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):
    a = distance(x1 = x1, y1 = y1, x2 = x2, y2 = y2)
    b = distance(x1 = x2, y1 = y2, x2 = x3, y2 = y3)
    c = distance(x1 = x3, y1 = y3, x2 = x1, y2 = y1)
        
    return triangleArea(a, b, c)

def lineIntersection(m1, b1, m2, b2):
    if (not almostEqual(m1, m2)):
        return (b2-b1)/(m1 - m2)    


def threeLinesArea(m1, b1, m2, b2, m3, b3):
    if (almostEqual(m1, m2)
        or almostEqual(m1, m3)
        or almostEqual(m2, m3)):
        return 0
    else:
        # Find x 
        x1 = lineIntersection(m1, b1, m2, b2)        
        x2 = lineIntersection(m2, b2, m3, b3)
        x3 = lineIntersection(m1, b1, m3, b3)

        # Find y 
        y1 = x1 * m1 + b1
        y2 = x2 * m2 + b2
        y3 = x3 * m3 + b3
        # print(x1, '', y1, '', x2, '', y2)

        # Find side length
        a = distance(x1 = x1, y1 = y1, x2 = x2, y2 = y2)
        b = distance(x1 = x2, y1 = y2, x2 = x3, y2 = y3)
        c = distance(x1 = x3, y1 = y3, x2 = x1, y2 = y1)
        # print(a, '', b, '', c)
        # calculate area        
        return triangleArea(a, b, c)

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    # check left, right, top, down
    Left = (x1 + w1 < x2)
    Right = (x2 + w2 < x1)
    Top = (y1 + h1 < y2)
    Down = (y2 + h2 < y1)

    if (Left or Right or Top or Down):
        return False
    else:
        return True  

#################################################
# Test Functions
#################################################

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print('Passed.')

def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assert(isEvenPositiveInt(809) == False)
    assert(isEvenPositiveInt(810) == True)
    assert(isEvenPositiveInt(2389238001) == False)
    assert(isEvenPositiveInt(2389238000) == True)
    assert(isEvenPositiveInt(-2389238000) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt('do not crash here!') == False)
    print('Passed.')

def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()... ', end='')
    assert(nthFibonacciNumber(0) == 1)
    assert(nthFibonacciNumber(1) == 1)
    assert(nthFibonacciNumber(2) == 2)
    assert(nthFibonacciNumber(3) == 3)
    assert(nthFibonacciNumber(4) == 5)
    assert(nthFibonacciNumber(5) == 8)
    assert(nthFibonacciNumber(6) == 13)
    print('Passed.')

def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assert(isLegalTriangle(3, 4, 5) == True)
    assert(isLegalTriangle(5, 4, 3) == True)
    assert(isLegalTriangle(3, 5, 4) == True)
    assert(isLegalTriangle(0.3, 0.4, 0.5) == True)
    assert(isLegalTriangle(3, 4, 7) == False)
    assert(isLegalTriangle(7, 4, 3) == False)
    assert(isLegalTriangle(3, 7, 4) == False)
    assert(isLegalTriangle(5, -3, 1) == False)
    assert(isLegalTriangle(-3, -4, -5) == False)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testTriangleArea():
    print('Testing triangleArea()... ', end='')
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(3,4,0), 0))
    assert(almostEqual(triangleArea(3,4,7), 0))
    assert(almostEqual(triangleArea(-3,-4,-5), 0))
    assert(almostEqual(triangleArea(1,2,2.8), (2.9 * 1.9 * 0.9 * 0.1)**0.5))
    print('Passed.')

def testTriangleAreaByCoordinates():
    print('Testing triangleAreaByCoordinates()... ', end='')
    assert(almostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16))
    assert(almostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250))
    assert(almostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),
                                                 4*3**.5))
    assert(almostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,-2,2,5,5),0))
    print('Passed.')

def testLineIntersection():
    print('Testing lineIntersection()... ', end='')
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    assert(almostEqual(lineIntersection(10,0,-4,15), 1.0714285714285714))
    print('Passed.')

def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testFabricYards()
    testFabricExcess()
    testIsEvenPositiveInt()
    testNthFibonacciNumber()
    testIsLegalTriangle()
    testIsRightTriangle()
    testTriangleArea()
    testTriangleAreaByCoordinates()
    testLineIntersection()
    testThreeLinesArea()
    testRectanglesOverlap()

def main():
    cs112_f19_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
