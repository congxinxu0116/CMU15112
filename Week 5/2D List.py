# 2 D List
# Create 2 D List
# Assume 2 D list are rectangular
## Static allocation
a = [[2,3,4],
     [5,6,7]
    ]
print(a)

# Dynamic (Variable-Length) Allocation
rows = 3
cols = 2

# Error: creates shallow copy
# Creates one unique row, 
#   the rest are aliases!!!
a = [ [0] * cols] * rows 

print("This SEEMS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("But see what happens after a[0][0]=42")
print("   a =", a)

## Review List comprehension:
a = [ ([0] * cols) for row in range(rows) ]
## is same as 
a = []
for rows in range(rows)
    a += [[0] * cols]

## Best Option:
def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

# Getting 2d List Dimension
# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print("a = ", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])
print("rows =", rows)
print("cols =", cols)

# Copying and aliasing 2d list
import copy

# Create a 2d list
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]

# Try to copy it
b = copy.deepcopy(a) # Correct!

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("And after a[0][0] = 9")
print("   a =", a)
print("   b =", b)

# Nested Looping Over 2d list
# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print("Before: a =", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])

# And now loop over every element
# Here, we'll add one to each element,
# just to make a change we can easily see
for row in range(rows):
    for col in range(cols):
        # This code will be run rows*cols times, once for each
        # element in the 2d list
        a[row][col] += 1

# Finally, print the results
print("After:  a =", a)

# Access 2d List by row or column
## Accessing a whole row
# alias (not a copy! no new list created)
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
row = 1
rowList = a[row]
print(rowList)

## Accessing a whole column
# copy (not an alias! new list created)
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
col = 1
colList = [ ]
for i in range(len(a)):
    colList += [ a[i][col] ]
print(colList)

## Accessing a whole column with a
##   list comprehension
# still a copy, but cleaner with a list comprehension!
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
col = 1
colList = [ a[i][col] for i in range(len(a)) ]
print(colList)

# non-rectangular ("ragged") 2d list
# 2d lists do not have to be rectangular
a = [ [ 1, 2, 3 ] ,
      [ 4, 5 ],
      [ 6 ],
      [ 7, 8, 9, 10 ] ]

rows = len(a)
for row in range(rows):
    cols = len(a[row]) # now cols depends on each row
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(a[row][col], " ", end="")
    print()


# 3 D Lists
# 2d lists do not really exist in Python.
# They are just lists that happen to contain other lists as elements.
# And so this can be done for "3d lists", or even "4d" or higher-dimensional lists.
# And these can also be non-rectangular, of course!

a = [ [ [ 1, 2 ],
        [ 3, 4 ] ],
      [ [ 5, 6, 7 ],
        [ 8, 9 ] ],
      [ [ 10 ] ] ]

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print("a[%d][%d][%d] = %d" % (i, j, k, a[i][j][k]))