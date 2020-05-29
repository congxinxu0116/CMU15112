# Code Tracing 

# CT1:
def f(x):
    print('f', x)
    x += 1
    return (x**2) // 10

def g(x):
    print('g', x)
    x = (7 * x) % 5
    return f(x + 3)

x = 5
print(f(g(f(x))) + x)
# Step 1 f(x)
# f(5) = 5 + 1 = 6 **2 = 36 //10 = 3

# Step 2 g(3)
# g(3)  = 3 * 7 mod 5 = 1 
# f(4) = 4 +1 = 5 ** 2 // 10 = 2

# Step 3 f(2)
# f(2) = 3 ** 2 //10 = 0

# Step 4 0 + 5 = 5

# CT2:

import math
print(1 * 2 // 1 + 4 - 3)
# 1*2 = 2 // 1 = 2 +4 = 6-3 = 3
print(2**4/10 + (3 + 2**3) // 10)
# 16/10 + (3 + 8) // 10 = 
#   1.6 + 11 //10 = 1.6 + 1 = 2.6
print(round(8/3) + max(8/3, math.ceil(8/3)))
# 2 2/3 = 3 + 3 = 6

# CT3:

def f(x, y):
    if (x > y):
        if (x > 2 * y): print('A')
        else: print('B')
    print('C')

def g(x, y):
    if (abs(x % 10 - y % 10) < 2): print('D')
    elif (x % 10 > y % 10): print('E')
    else:
        if (x // 10 == y // 10): print('F')
        if (x // y > 0): print('G')
f(3,4)
# C
g(1,2)
# D

# CT4:

def f(x): 
    return 3 * x - 2

def g(x): 
    return f(x + 3)

def h(x):
    print(f(x - 2))
    x -= 2
    print(g(x))
    x %= 4
    return f(g(x) % 6) // 2

print(3 + h(4))
# Step 1 h(4)
# print(f(2))
# f(2) = 3*2-2 = 4 # print 1
# x = x - 2 = 2
# print(g(2))
# g(2) = f(5)
# f(5) = 3*5-2 = 13 # print 2
# x = x mod 4 = 2
# return f(g(2) % 6) // 2
# g(2) = 13 % 6 = 1
# f(1) = 3*1 -2 = 1 // 2 = 0 # return
# final print 3 + 0 = 3

# CT5:

def f(x): 
    return 2 * x + 1

def g(x): 
    return f(x // 2)

def h(x):   
    if (x % 2 == 0): 
        return f(x + g(x))   
    else:   
        return f(x) - g(x)
def ct(x):
    print(h(x))
    print(h(x + 1))
print(ct(5))
# Step 1 Ct(5)
# print(h(5))
#   h(5) = f(5) - g(5)
#        = 2*5+1 - h(5//2)
#        = 11 - 2*2+1
#        = 11 - 5 = 6# CT5:
print("=====================")
def f(x): 
    return 2 * x + 1

def g(x): 
    return f(x // 2)

def h(x):   
    if (x % 2 == 0): 
        return f(x + g(x))   
    else:   
        return f(x) - g(x)
def ct(x):
    print(h(x))
    print(h(x + 1))
print(ct(5))
# print(h(6))
#   h(6) = f(6 + g(6))
#        = f(6 + f(6 // 2))
#        = f(6 + f(3))
#        = f(6 + 2*3+1)
#        = f(6+7)
#        = 2*13+1 = 27
# return None since there is no return 
#   statement in ct()

# Reasoning Over Code (ROC)
# Find values for the parameters so the
#   functions return True
def rc1(x, y):
    return ((100 > x > y > 0) and 
            (x + y == 10) and 
            (y // x == x // y - 1))

print(rc1(6,4))

def rc2(x):
    return ((type(x) == int) and 
            (int(round(x**0.5))**2  ==  x) and 
            (x//10 == x%10 + 2))

# Square and first digit - second digit = 2
print(rc2(64))

def rc3(x, y):
    return ((type(x) == type(y) == int) and
            (100 > x > y > 0) and
            (x % 10 == y // 10) and
            (y % 10 == x // 10) and
            (x - y == 9))

print(rc3(43, 34)) # print(rc3(32, 23))

#
def almostEqual(x, y):
    return abs(x - y) < 10**-9

def rc4(n):
    if ((not isinstance(n, int)) or (n < 100) or (n > 999)): 
        return False
    a = n % 10
    b = n // 10
    return (almostEqual(b**0.5, a) and (a + b ==  42))
print(rc4(366))

def rc5(x):
    assert(type(x) == int)
    return ((x % 10 == x // 10 - 1) and (x // 9 * 9 == x))

print(rc5(54))