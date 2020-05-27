# This is a comment

print('Hello World')

print('Carpe')
print("diem")

# separate multiple values with commas

print("Guoguo", "Minying")

# end = "" to stay on the same line 
print("Guoguo ", end = "")
print("minying")

# Print using f strings
x = 52
t = 33

# place variable names in {squiggly braces} 
#   to print their values 
print(f'Do you know that {x} + {t} is {x + t}')

# import modules
# print(math.factorial(20))

# import modules/packages
import math
print(math.factorial(20))

# basic console input
# name = input("Enter you name: ")
# print("Your name is:", name)

# input a number (ERROR)
x = int(input("Enter a number: "))
print("One half of", x, "=", x/2)