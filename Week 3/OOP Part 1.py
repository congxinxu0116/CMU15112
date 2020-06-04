### Object Oriented Programming Part 1 ###
# using Objects and Methods 

# We call methods using s.f() rather than f(s)

s = 'This could be any string!'

print(len(s))     # len is a function

print(s.upper())  # upper is a string method, called using the . notation
                  # we say that we "call the method len on the string s"

print(s.replace('could', 'may')) # some methods take additional arguments

# See how we get different erros for improperly calling methods vs. functions
n = 123
print(len(str(n)))    # TypeError: object of type 'int' has no len()
                 # This means that len() cannot work properly with int's

n = 123
print(str(n).upper()) # AttributeError: 'int' object has no attribute 'upper'
                 # This means that there is no method upper() for int's