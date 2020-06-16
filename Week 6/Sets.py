# Sets 

# Quick Example
# Sets are un-ordered
s = set([2,3,5])
print(3 in s)
print(4 in s)

for x in range(7):
    if (x not in s):
        print(x)

# print(s[0]) # Crash, sets does not support indexing

# Create sets
S = set() # Empty sets
W = {'cat', "cow", 'dog'}
print(W)
print(type(W))
print(S)

print(set("wahoo")) # print {'w', 'o', 'a', 'h'}

# Create an empty set
s = set()
print(s)

# Create a set from a list
s = set(['cat', "cow", 'dog'])

# Create a statically-allocated set
s = {2,3,5}
print(s)

# Caution: {} is not an empty set!
s = { }
print(type(s) == set)
print(type(s)) # This is a dictionary  

# Use Sets
# Sets can do many of the same things as lists and tuples...
s = set([1, 2, 3])

print(len(s)) # prints 3

print(2 in s) # prints True
print(4 in s) # prints False
print(4 not in s) # prints True
print(2 not in s) # prints False

s.add(7)      # use add instead of append to add an element to a set
s.remove(3)   # removes 3 from the set; raises an error if 3 is not in s

for item in s:
    print(item) # we can loop over the items in s

# Property of Sets

# Hash Functions
# hash(x) --> integer

# Sets are made of buckets
# |______| |"hello"| |"world", 42| |______|
#     0        1        2        3 
# Adding an element to a set 
# hash("hello") --> 1151755633 % 4 --> 1
#                                ^ 4 is the number of buckets
# hash("world") --> 1811521994 % 4 --> 2
# hash(42) --> 42 % 4 --> 2

## Sets are unordered
S = set(["hello", "world", 42])
print(S)

print(set([1,2,3]) == set([3,2,1]))

# Elements are unqiue
S = set([2,2,2])
print(S)
print(len(S))

# Elements Must be Immutable

# Sets can only hold elements that are immutable (cannot be changed),
# such as numbers, booleans, strings, and tuples
a = ["lists", "are", "mutable"]
# s = set([a])       # TypeError: unhashable type: 'list'
# print(s)

# Hashing
# 0. Preliminaries
import time
n = 10000

# 1. Create a list [2,4,6,...,n] then check for membership
# among [1,2,3,...,n] in that list.

# don't count the list creation in the timing
a = list(range(2,n+1,2))

print("Using a list... ", end="")
start = time.time()
count = 0
for x in range(n+1):
    if x in a:
        count += 1
end = time.time()
elapsed1 = end - start
print("count=", count," and time = %0.4f seconds" % elapsed1)

# 2. Repeat, using a set
print("Using a set.... ", end="")
start = time.time()
s = set(a)
count = 0
for x in range(n+1):
    if x in s:
        count += 1
end = time.time()
elapsed2 = end - start
print("count=", count," and time = %0.4f seconds" % elapsed2)
print("With n=%d, sets ran about %0.1f times faster than lists!" %
      (n, elapsed1/elapsed2))
print("Try a larger n to see an even greater savings!")

# Worked Example Using Sets

def isPermutation(L):
    # return True if L is a permutation of [0,...,n-1]
    # and False otherwise
    return (set(L) == set(range(len(L))))

def testIsPermutation():
    print("Testing isPermutation()...", end="")
    assert(isPermutation([0,2,1,4,3]) == True)
    assert(isPermutation([1,3,0,4,2]) == True)
    assert(isPermutation([1,3,5,4,2]) == False)
    assert(isPermutation([1,4,0,4,2]) == False)
    print("Passed!")

testIsPermutation()


def repeats(L):
    # return a sorted list of the repeat elements in the list L
    seen = set()
    seenAgain = set()
    for element in L:
        if (element in seen):
            seenAgain.add(element)
        seen.add(element)
    return sorted(seenAgain) # convert set to list and ordered it

def testRepeats():
    print("Testing repeats()...", end="")
    assert(repeats([1,2,3,2,1]) == [1,2])
    assert(repeats([1,2,3,2,2,4]) == [2])
    assert(repeats(list(range(100))) == [ ])
    assert(repeats(list(range(100))*5) == list(range(100)))
    print("Passed!")

testRepeats()