#################################################
# hw8.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week8_linter
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

def getPairSum(lst, target):
    if (len(lst) > 1):
        s = set()
        for i in lst:
            if (target - i in s):
                return (i, target - i)
            else:
                s.add(i)

def containsPythagoreanTriple(lst):
    lst = [i**2 for i in lst]
    # print(lst)
    if (len(lst) > 2):
        s = set()
        i = 0
        while (i < len(lst)):
            j = i + 1
            while (j < len(lst)):
                if (lst[i] + lst[j] in s 
                    or abs(lst[i] - lst[j]) in s):                    
                    return True
                else:
                    s.add(lst[i])
                    s.add(lst[j])
                # print(i, j)
                j += 1
            i += 1
    return False

def movieAwards(oscarResults):
    d = dict()
    for i in oscarResults:
        tmp = 1 + d.get(i[1], 0)
        d[i[1]] = tmp
    return d

def friendsOfFriends(d):
    output = dict()
    for i in d: # self
        output[i] = set()
        for j in d[i]:
            for k in d[j]:
                if (k not in d[i] 
                    and k != i):
                    output[i].add(k)
    return output

#################################################
# Test Functions
#################################################

def testgetPairSum():
    print('Testing testgetPairSum()... ', end='')
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in
             [ (10, -8), (-8, 10), (-1, 3), (3, -1), (1, 1) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    print('Passed.')

def testcontainsPythagoreanTriple():
    print('Testing containsPythagoreanTriple()... ', end='')
    assert(containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]) == True)
    assert(containsPythagoreanTriple([1, 3, 6, 2, 1, 4]) == False)
    assert(containsPythagoreanTriple([5,1,8,2,12,13,4]) == True)
    
    print('Passed.')

def testmovieAwards():
    print('Testing movieAwards()... ', end='')
    a = { 
        ("Best Picture", "Green Book"), 
        ("Best Actor", "Bohemian Rhapsody"),
        ("Best Actress", "The Favourite"),
        ("Film Editing", "Bohemian Rhapsody"),
        ("Best Original Score", "Black Panther"),
        ("Costume Design", "Black Panther"),
        ("Sound Editing", "Bohemian Rhapsody"),
        ("Best Director", "Roma")
    }   

    b = { 
        "Black Panther" : 2,
        "Bohemian Rhapsody" : 3,
        "The Favourite" : 1,
        "Green Book" : 1,
        "Roma" : 1
    }
    assert(movieAwards(a) == b)
    
    print('Passed.')

def testfriendsOfFriends():
    print('Testing friendsOfFriends()... ', end='')
    d = { }
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()   

    e = {
        'tyrion': {'arya', 'brienne'}, 
        'pod': {'jon'}, 
        'brienne': {'tyrion'}, 
        'arya': {'tyrion'}, 
        'jon': {'pod', 'jaime'}, 
        'jaime': {'pod', 'jon'}, 
        'ramsay': set()
        }
    assert(movieAwards(d) == e)
    
    print('Passed.')
#################################################
# testAll and main
#################################################

def testAll():
    testgetPairSum()
    testcontainsPythagoreanTriple()
    testmovieAwards()
    print("All Good")

def main():
    cs112_f19_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
