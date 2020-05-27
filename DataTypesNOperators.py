### Data Types and Operators ###
# Some builtin Types
import math

def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python")
print(type(2))             # int
print(type(2.2))           # float
print(type(2 < 2.2))       # boolean
print(type(type(42)))      # type

print("######################################")
print("And some other types we",
      "may see later in the course...")
print(type("2.2"))         # string or text
print(type([1,2,3]))       # list
print(type((1,2,3)))       # tuple
print(type({1,2,3}))       # set
print(type({1:42}))        # dictionary or map
print(type(2 + 3j))        # complex number

# some built in operators 
# integer division 
print(7//4) # = 1
print(-7//4) # = -2

# integer division is same as math.floor() and /
import math
print(math.floor(-7/4))

# double start ** is exponentiation 
print(2**3) # = 8

# % is mod, 9 mod 5 is going to be 4
#   because 9 divided by 5, the remainder is 4
print(9 % 5)

# 
x = 2
x += 1
# += is same as x = x + 1
print(x) # 3

# the modulus or Remainder Operator %
# verify that (a%b) is equivalent to (a - (a//b)*b)

def mod(a , b):
    return a - (a//b) * b

print(41%14, mod(41,14))
print(14%41, mod(14,41))
print(-32%9, mod(-32,9))
print(32%-9, mod(32,-9))

# Type affect semantics 
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
# print(3 + "def")

# Approximate Vlaues of Floating-Point Numbers
print(0.1 + 0.1 == 0.2 )
print(0.1 + 0.1 + 0.1 == 0.3) # FALSE?????
print(0.1 + 0.1 + 0.1)  

def almostEqual (x ,y):
    epsilon = 10**-8
    return(abs(x - y) < epsilon)

print(almostEqual(x = 0.1+0.1+0.1, y = 0.3))


# short circuit evaluation 
# When using "and", if the left is a false, 
#   python will not evaluate what on the right of 
#   the "and"
def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,") =", result)
    return result

def isEven(n):
    result = (n % 2 == 0)
    print("isEven(",n,") =", result)
    return result

print("Test 1: isEven(-4) and isPositive(-4))")
# Calls both functions
print(isEven(-4) and isPositive(-4)) 
print("----------")

# Calls only one function!
print("Test 2: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3)) 

# Both type and isinstance can be used to type-check
# In general, (isinstance(x, T)) will be more robust
#   than (type(x) == T)

print(type("abc") == str)
print(isinstance("abc", str))

# We'll see better reasons for this when we cover OOP + inheritance later
# in the course.  For now, here is one reason:  say you wanted to check
# if a value is any kind of number (int, float, complex, etc). 
# You could do:

def isNumber(x):
    return ((type(x) == int) or
            (type(x) == float)) # are we sure this is ALL kinds of numbers?

print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))

# But this is cleaner, and works for all kinds of numbers, including
# complex numbers for example:

import numbers
def isNumber(x):
    return isinstance(x, numbers.Number) # works for any kind of number

print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))