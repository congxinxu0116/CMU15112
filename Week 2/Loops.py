# For Loop and Range
# A for loop repeats an action a specific number of 
#   times based on the provided range
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):
        total += x
    return total

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# Actually no need for a loop 
def sumFromMToN2(m, n):
    return sum(range(m, n+1))

print(sumFromMToN2(5, 10) == 5+6+7+8+9+10)

def sumToN(n):
    return n*(n+1) // 2

def sumFromMToN_byFormula(m, n):
    return (sumToN(n) - sumToN(m - 1))

print(sumFromMToN_byFormula(5, 10) == 5+6+7+8+9+10)

# what if we omit the first parameter
def sumToN(n):
    total = 0
    # range defaults the starting number to be 0
    for x in range(n+1):
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)

# What if we add a third parameter?
def sumEveryKthFromMToN(m, n, k):
    total = 0
    # the third parameter becomes a step
    for x in range(m, n+1, k):
        total += x
    return total

print(sumEveryKthFromMToN(5, 20, 7) == 
      (5 + 12 + 19)) 

# Sum just odd number from m to n
def sumOfOddsFromMToN(m, n):
    total = 0
    if (m % 2 == 0):
        m += 1
    for i in range(m, n+1, 2):
        total += i 
    return total

# We can also change the step by changing the 
#   inside of the loop
def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(m, n+1):
        if (x % 2 == 1):
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == 
        sumOfOddsFromMToN(5,9) == 
        (5+7+9))

# Here we will range in reverse
# (not wise in this case, but instructional)
def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(n, m-1, -1):
        if (x % 2 == 1):
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == 
      sumOfOddsFromMToN(5,9) == 
      (5+7+9))

# Nested for Loops
def printCorrdinates(xMax, yMax):
    for x in range(xMax + 1):
        for y in range(yMax + 1):
            print("(", x, ",", y, ")", end = "")
        print()

printCorrdinates(4, 5)

# Print Star Recntangle
def printStarRectangel(n):
    # print an n by n rectangel of asterisks
    for row in range(n):
        for col in range(n):
            print("*", end = "")
        print()

printStarRectangel(5)

# Mystery Star Shape
def printMysteryStarShape(n):
    for row in range(n):
        print(row, end = "")
        for col in range(row):
            print("*", end = "")
        print()
printMysteryStarShape(5)

# While Loop 
# use while loops when there is an indeterminate 
#   number of iterations
def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n // 10
    return n
print(leftmostDigit(72658489290098) == 7)

# Example: nth positive integer with some property
#   find the nth number that is a multiple of 
#   either 4 or 7 

def isMultipleOf4or7 (x):
    return (((x % 4) == 0) or ((x % 7) == 0))

def nthMultipleOf4or7 (n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (isMultipleOf4or7(guess)):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
print() # line break

# break and continue
# continue, break and pass are three keywords 
# used in loops in order to change the program flow
for n in range(200):
    if (n % 3 == 0):
        continue # skip the rest of this pass
    elif (n == 8):
        break # skips rest of entire loop
    else: 
        pass # does nothing! pass is a place holder
             #   not needed here
    print(n, end = " ")
print() # line break again 

# infinite while loop wih break 
def readUntilDone():
    linesEntered = 0
    while (True):
        response = input("Enter a string (or 'done' to quit): ")
        if (response == 'done'):
            break
        print(" You entered: ", response)
        linesEntered += 1
    print("Bye")
    return linesEntered

# linesEntered = readUntilDone()
# print("You entered", linesEntered, "lines (not counting 'done').")

# isPrime
# simple and clear way, not the fastest/best way
def isPrime(n):
    if (n < 2):
        return False
    for factor in range (2, n):
        if (n % factor == 0):
            return False
    return True

for n in range(100):
    if isPrime(n):
        print(n, end = " ")

print()

# This is still not the fastest way, but 
#   it's a nice improvement
def fasterIsPrime(n):
    if (n < 2):
        return False 
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n ** 0.5)
    for factor in range(3, maxFactor + 1, 2):
        if (n % factor == 0):
            return False
    return True

# And try out this version:
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()

# Verify these are the same
for n in range(100):
    assert(isPrime(n) == fasterIsPrime(n))
print("They seem to work the same!")

# Now let's see if we really sped things up
import time
bigPrime = 499 # Try 1010809, or 10101023, or 102030407
print("Timing isPrime(",bigPrime,")", end=" ")
time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ",(time1-time0)*1000,"ms")

print("Timing fasterIsPrime(",bigPrime,")", end=" ")
time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ",(time1-time0)*1000,"ms")


# adapt the "nth" pattern we used above in 
#   nthMultipleOf4or7()
def nthPrime (n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (fasterIsPrime(guess)):
            found += 1
    return guess

# and let's see a list of the primes
for n in range(10):
    print(n, nthPrime(n))
print("Done!")