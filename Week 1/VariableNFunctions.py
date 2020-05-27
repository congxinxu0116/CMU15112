### Variable and Functions ###

# Variables
# A variable is a named value that references
#   or stores a piece of data

# Unlike in math, variables can have new values
#   assigned to them, even values of different types
y = 10 
print(y - 2)

y = True
print(y)
# Variable can be given any names, as long as it 
#   starts with a letter and contains no special 
#   characters

# variables can be updated with assignment operations
x = 5 
x += 2 # same as x = x + 2
print(x) # shouold be 7

y = 350 
y //= 10 # same as y = y // 10, integer divide
print(y)

# A function is composed of two parts: the header and the body.

# The header defines the name and parameters.
# A function header is written as follows: def functionName(parameters):
# The parameters are variables that will be provided when the function is called.
# The header ends with a colon to indicate that a body will follow.

# The body contains the actions (statements) that the function performs.
# The body is written under the function with an indent.
# When the lines are no longer indented, the function body ends.
# Functions usually contain a return statement. This will provide the result when the function is called.

# Example:

def double(x):
    print("I'm in the double function!")
    return 2 * x

# To call the function, we use the function's name,
# followed by parentheses which contain the data values we want to use, called function arguments.
# This function call will evaluate to an expression.

print(double(2)) # will print 4
print(double(5)) # will print 10
print(double(1) + 3) # will print 5

# Some functions are already provided by Python

print("Type conversion functions:")
print(bool(0))   # convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8))  # convert to an integer (int)

print("And some basic math functions:")
print(abs(-5))   # absolute value
print(max(2,3))  # return the max value
print(min(2,3))  # return the min value
print(pow(2,3))  # raise to the given power (pow(x,y) == x**y)
print(round(2.354, 1)) # round with the given number of digits


# In general, you should avoid using global variables.
# You will even lose style points if you use them!
# Still, you need to understand how they work, since others
# will use them, and there may also be some very few occasions
# where you should use them, too!

g = 100

def f(x):
    return x + g

print(f(5)) # 105
print(f(6)) # 106
print(g)    # 100

# Another example

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102, because we call f() twice

def f(x):
    x + 42
# The function will return N-o-n-e if there is no return
print(f(4)) # N-o-n-e

d1 = 0.1 + 0.1 + 0.1
d2 = 0.3

def almostEqual(x, y):
    return abs(x - y) < 10**-9

# This will now work properly!
print(almostEqual(0, 0.0000000000001))
print(almostEqual(d1, d2))
