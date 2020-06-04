# String Literals
# 1. Four kinds of quotes
# Quotes enclose characters to tell Python "this is a string!"
# single-quoted or double-quoted strings are the most common
print('single-quotes')
print("double-quotes")

# triple-quoted strings are less common (though see next section for a typical use)
print('''triple single-quotes''')
print("""triple double-quotes""")

# The reason we have multiple kinds of quotes is partly so we can have strings like:
print('The professor said "No laptops in class!" I miss my laptop.')

# 2. New lines in strings 
# A character preceded by a backslash, like \n, is an 'escape sequence'.
# Even though it looks like two characters, Python treats it as one special character.

# Note that these two print statements do the same thing!
print("abc\ndef")  # \n is a single newline character.
print("""abc
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

# 3. More Escape Sequences
print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")

s = "a\\b\"c\td"
print("s =", s)
print("len(s) =", len(s))

print("These look the same when we print them!")
s1="abc\tdef"
s2="abc  def"

print("print s1: ",s1)
print("print s2: ",s2)


print("\nThey aren't really though...")
print("s1==s2?", s1==s2)

print("\nLet's try repr instead")
print("repr s1: ",repr(s1))
print("repr s2: ",repr(s2))


print("\nHere's a sneaky one")
s1="abcdef"
s2="abcdef             \t"

print("print s1: ",s1)
print("print s2: ",s2)

print("s1==s2?", s1==s2)

print("repr s1: ",repr(s1))
print("repr s2: ",repr(s2))
print("repr() lets you see the spaces^^^")

# string Literals as Multi-line comments
"""
Python does not have multiline comments, but you can do something similar
by using a top-level multiline string, such as this. Technically, this is
not a comment, and Python will evaluate this string, but then ignore it
and garbage collect it!
"""
print("wow!")

# Some String Constants

import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)       # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)      # space + tab + linefeed + return + ...

# Some string operators

# String plus + and multiply *
print("abc" + "def")  # What do you think this should do?
print("abc" * 3)  # How many characters do you think this prints?
# print("abc" + 3)  # ...will this give us an error? (Yes)

# The inn operator 
# The "in" operator is really really useful!
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")


# String indexing and slicing
## 1. indexing a sinlge character
# Indexing lets us find a character at a specific location (the index)
s = "abcdefgh"
print(s)
print(s[0])
print(s[1])
print(s[2])

print("-----------")
print("Length of ",s,"is",len(s))

print("-----------")
print(s[len(s)-1])
## print(s[len(s)])  # crashes (string index out of range)

## Negative indexs 
s = "abcdefgh"
print(s)
print(s[-1])
print(s[-2])

## Slicing a range of characters
# Slicing is like indexing, but it lets us get more than 1 character.
# ...how is this like range(a,b)?

s = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print("-----------")
print(s[2:3])
print(s[3:3]) # prints nothing 

## Slicing with default parameters
s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:])

## Slicing with a step parameter
print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])

## Reversing a string

s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")

def reverseString(s):
    return s[::-1]

print(reverseString(s)) # crystal clear!

# Looping over Strings
## For loop with indexes
s = "abcd"
for i in range(len(s)):
    print(i, s[i])

# for loop without indexes
s = "abcd"
for c in s:
    print(c)

# for loop with split
# By itself, names.split(",") produces something called a list.
# Until we learn about lists (soon!), do not store the result of
# split() and do not index into that result.  Just loop over the
# result, as shown here:

names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)

# for loop with splitlines
# splitlines() also makes a list, so only loop over its results,
# just like split():

# quotes from brainyquote.com
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if (line.startswith("Knuth")):
        print(line)

# Example: IsPalindrome
# A string is a palindrome if it is 
#    exactly the same forwards and backwards
# There are many ways to write isPalindrome(s)
# Here are several.  Which way is best?

def reverseString(s):
    return s[::-1]

def isPalindrome1(s):
    return (s == reverseString(s))

def isPalindrome2(s):
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

def isPalindrome3(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]):
            return False
    return True

def isPalindrome4(s):
    while (len(s) > 1):
        if (s[0] != s[-1]):
            return False
        s = s[1:-1]
    return True

print(isPalindrome1("abcba"), isPalindrome1("abca"))
print(isPalindrome2("abcba"), isPalindrome2("abca"))
print(isPalindrome3("abcba"), isPalindrome3("abca"))
print(isPalindrome4("abcba"), isPalindrome4("abca"))

# Strings are Immutable 
## You cannot change strings! They are immutable
s = "abcde"
# s[2] = "z"  # Error! Cannot assign into s[i]

## Instead, you must create a new string.
s = "abcde"
s = s[:2] + "z" + s[3:]
print(s)

# Some string-related Built-In Functions
## str() convert number into string
## len() get the length of a string

# name = input("Enter your name: ")
# print("Hi, " + name + ". Your name has " 
#        + str(len(name)) + " letters!")

## chr() converts a ordered number into character
## ord() converts a string into a ordered number
print(ord("A")) # 65
print(chr(65))  # "A"
print(chr(ord("A")+1)) # "B"

## eval()
# eval() works but you should not use it!
s = "(3**2 + 4**2)**0.5"
print(eval(s))

# why not? Well...
# s = "reformatMyHardDrive()"
# print(eval(s)) # no such function!  But what if there was?


# Some string methods
# value.function() is a method not a function, but similar
# Run this code to see a table of isX() behaviors
def p(test):
    print("True     " if test else "False    ", end="")
def printRow(s):
    print(" " + s + "  ", end="")
    p(s.isalnum()) # is alphabetical and numeric
    p(s.isalpha()) # is alphabetical
    p(s.isdigit())
    p(s.islower())
    p(s.isspace()) # space, new line and tab
    p(s.isupper())
    print()
def printTable():
    print("  s   isalnum  isalpha  isdigit  islower  isspace  isupper")
    for s in "ABCD,ABcd,abcd,ab12,1234,    ,AB?!".split(","):
        printRow(s)
printTable()

## String edits: lower(), upper(), replace(), strip()
print("This is nice. Yes!".lower())
print("So is this? Sure!!".upper())
print("   Strip removes leading and trailing whitespace only    ".strip())
print("This is nice.  Really nice.".replace("nice", "sweet"))
print("This is nice.  Really nice.".replace("nice", "sweet", 1)) # count = 1

print("----------------")
s = "This is so so fun!"
t = s.replace("so ", "")
print(t)
print(s) # note that s is unmodified (strings are immutable!)


## Substring search: count(), startswith(), 
##   endswith(), find(), index()
print("This is a history test".count("is")) # 3
print("This IS a history test".count("is")) # 2
print("-------")
print("Dogs and cats!".startswith("Do"))    # True
print("Dogs and cats!".startswith("Don't")) # False
print("-------")
print("Dogs and cats!".endswith("!"))       # True
print("Dogs and cats!".endswith("rats!"))   # False
print("-------")
print("Dogs and cats!".find("and"))         # 5
print("Dogs and cats!".find("or"))          # -1
print("-------")
print("Dogs and cats!".index("and"))        # 5
# print("Dogs and cats!".index("or"))         # crash!

# String Formatting
## format a string with %s 
breed = "beagle"
print("Did you see a %s?" % breed)

## format an integer with %d 
dogs = 42
print("There are %d dogs." % dogs)

## format a float with %f
grade = 87.385
print("Your current grade is %f!" % grade)

## format a float with %.[precision]f
grade = 87.385
print("Your current grade is %0.1f!" % grade)
print("Your current grade is %0.2f!" % grade)
print("Your current grade is %0.3f!" % grade)
print("Your current grade is %0.4f!" % grade)

## format multiple values
dogs = 42
cats = 18
exclamation = "Wow"
print("There are %d dogs and %d cats. %s!!!" % (dogs, cats, exclamation))

## format right-aligned with %[minWidth]
dogs = 42
cats = 31

print("%10s %10s" % ("dogs", "cats"))
print("%10d %10d" % (dogs, cats))

## format left-aligned with %-[minWidth]
dogs = 42
cats = 3
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))

## String Formatting with f Strings
# We saw this example back in week1!
# It shows a nice relatively new way to format strings:

x = 42
y = 99
# Place variable names in {squiggly braces} to print their values, like so:
print(f'Did you know that {x} + {y} is {x+y}?')

# Basic File IO

# Note: As this requires read-write access to your hard drive,
#       this will not run in the browser in Brython.

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)