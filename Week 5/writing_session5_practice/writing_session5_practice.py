#################################################
# writing_session5_practice_solutions.py
#################################################

import cs112_f19_week5_linter
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
def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    output = make2dList(len(A) - 1, len(A[0]) - 1)
    
    i = 0
    found_i = 0 
    while (i < len(output)):        
        if (i == row):        
            j = 0
            found_i += 1
            found_j = 0
            while (j < len(output[0])):
                if (j == col):
                    output[i][j] = A[i+1][j + 1]
                    found_j += 1
                    j += 1
                else:
                    output[i][j] = A[i+1][j + found_j]
                    j += 1            
        else:
            j = 0
            found_j = 0
            while (j < len(output[0])):
                if (j == col):
                    output[i][j] = A[i + found_i][j + 1]
                    found_j += 1
                    j += 1
                else:
                    output[i][j] = A[i + found_i][j + found_j]
                    j += 1
        i += 1    
    return output

def destructiveRemoveRowAndCol(A, row, col):
    # remove row
    A.pop(row)
    
    # remove column
    i = 0
    while (i < len(A)):
        j = 0
        while (j < len(A[0])):
            if (j == col):
                A[i].pop(j)
            j += 1
        i += 1

def calculateQuiz(a, col):
    i = 0
    count = 0
    total = 0
    while(i < len(a)):
        if (a[i][col] != -1):
            count += 1
            total = total + a[i][col]
        i += 1
    
    if (count != 0):
        return total / count  
    else:
        return -1
        
def bestQuiz(a):
    i = 0
    best = 0
    bestQuiz = 0
    while (i < len(a[0])):
        tmp = calculateQuiz(a, i)
        if (tmp > best):
            best = tmp
            bestQuiz = i
        i += 1
    
    if (best > 0):
        return bestQuiz


def matrixAdd(L, M):
    if (len(L) == len(M) and len(L[0]) == len(M[0])):
        output = make2dList(len(L), len(L[0]))
        i = 0
        while (i < len(output)):
            j = 0
            while (j < len(output[0])):
                output[i][j] = L[i][j] + M[i][j]
                j += 1
            i += 1

        return output

def sumOverCol(a, col):
    i = 0
    total = 0
    while (i < len(a)):
        total = total + a[i][col]
        i += 1
    
    return total

def isMostlyMagicSquare(a):
    # Check each row
    i = 0
    check_row = 0
    while (i + 1 < len(a)):
        if (sum(a[i]) == sum(a[i + 1])):
            check_row += 1
        i += 1
    
    # Check each column
    j = 0
    check_col = 0
    while (j + 1 < len(a[0])):
        if(sumOverCol(a, j) == sumOverCol(a, j + 1)):
            check_col += 1
        j += 1
    
    # Check each diaonals
    k = 0
    sumOfDia1 = 0
    sumOfDia2 = 0
    ## Calculate the sum of diagonal 1
    while (k < len(a)):
        sumOfDia1 = sumOfDia1 + a[k][k]
        sumOfDia2 = sumOfDia2 + a[k][len(a[0]) - k - 1]
        k += 1

    if (check_row == len(a) - 1 
        and check_col == len(a[0]) - 1
        and sumOfDia1 == sumOfDia2):
        return True
    else:
        return False

class DataTable(object):
    def __init__(self, csvString):
        # load the 2d list from the csv string
        self.data = csvString.split()
        i = 0
        while (i < len(self.data)):
            self.data[i] = self.data[i].split(",") 
            i += 1   
        # and convert the strings to numbers (but skip the labels)
        j = 1
        while (j < len(self.data)):
            k = 1
            while(k < len(self.data[j])):
                self.data[j][k] = int(self.data[j][k])
                k += 1
            j += 1

    def getDims(self):
        rows = len(self.data)
        cols = len(self.data[0])
        return rows, cols

    def getColumn(self, columnIndex):
        
        return DataColumn(self, columnIndex)

class DataColumn(object):
    def __init__(self, dataTable, columnIndex):
        self.label = dataTable.data[0][columnIndex]
        self.data = []
        
        i = 1
        while (i < len(dataTable.data)):
            self.data = self.data + [dataTable.data[i][columnIndex]]
            i += 1

    def average(self):
        return sum(self.data)/len(self.data)

#################################################
# Test Functions
#################################################

def testNondestructiveRemoveRowAndCol():
    print('Testing removeRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testBestQuiz():
    print('Testing bestQuiz()...', end='')
    a = [ [ 88,  80, 91 ],
          [ 68, 100, -1 ]]
    aCopy = copy.copy(a)
    assert(bestQuiz(a) == 2)
    assert(a == aCopy) # must be non-destructive!
    a = [ [ 88,  80, 80 ],
          [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88, -1, -1 ],
          [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1, -1, -1 ],
          [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    assert(bestQuiz([[]]) == None)
    print('Passed')

def testMatrixAdd():
    print('Testing matrixAdd()...', end='')
    L = [ [1,  2,  3],
          [4,  5,  6] ]
    M = [ [21, 22, 23],
          [24, 25, 26]]
    N = [ [1+21, 2+22, 3+23],
          [4+24, 5+25, 6+26]]
    lCopy = copy.copy(L)
    mCopy = copy.copy(M)
    assert(matrixAdd(L, M) == N)
    assert((L == lCopy) and (M == mCopy)) # must be non-destructive!
    assert(matrixAdd(L, [ [ 1, 2, 3] ]) == None) # dimensions mismatch
    print('Passed!')

def testIsMostlyMagicSquare():
    print("Testing isMostlyMagicSquare()...", end="")
    assert(isMostlyMagicSquare([[42]]) == True)
    assert(isMostlyMagicSquare([[2, 7, 6],
                                [9, 5, 1],
                                [4, 3, 8]]) == True)
    assert(isMostlyMagicSquare([[4-7, 9-7, 2-7],
                                [3-7, 5-7, 7-7],
                                [8-7, 1-7, 6-7]]) == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMostlyMagicSquare(a))
    assert(isMostlyMagicSquare([[1, 2], [2, 1]]) == False) # bad diagonals!
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMostlyMagicSquare(a) == False) # it's close, but not quite!
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMostlyMagicSquare(a) == False) # ditto!
    print("Passed!")

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))

    column0 = dataTable.getColumn(0)
    assert(isinstance(column0, DataColumn))
    assert(column0.label == 'Name')
    assert(column0.data == ['Fred', 'Wilma'])

    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testMatrixAdd()
    testIsMostlyMagicSquare()
    testDataTableAndDataColumnClasses()

def main():
    cs112_f19_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
