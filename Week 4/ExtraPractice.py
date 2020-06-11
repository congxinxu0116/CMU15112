# Week 4 
# Extra Practice 
# http://www.kosbie.net/cmu/fall-19/15-112/notes/extra-practice4.html


###################################################
def isPalindromicList(a):
    revA = a + [ ]
    a.reverse()
    if (a == revA):
        return True
    else:
        return False

assert(isPalindromicList([1,2,1]) == True)
assert(isPalindromicList([1,1]) == True)
assert(isPalindromicList([1,2,3,1]) == False)
assert(isPalindromicList([1,2,3,2,1]) == True)
assert(isPalindromicList([]) == True)
assert(isPalindromicList([1]) == True)


def reverse(a):
    length = len(a)
    i = 0
    while (i < length):
        a.append(a[length - 1 - i])
        a.pop(length - 1 - i)
        # print(a)
        i += 1
a = [234,5252,6,35,47,47,243]
a.reverse()
# print(a)
b = [234,5252,6,35,47,47,243]
reverse(b)
assert(a == b)

a = [3]
a.reverse()
# print(a)
b = [3]
reverse(b)
assert(a == b)

###################################################
def vectorSum(a, b):
    i = 0
    total = []
    while (i < len(a)):
        tmp = a[i] + b[i]
        total = total + [tmp]
        i += 1
    return total

assert(vectorSum([2,4], [20,30]) == [22,34])
assert(vectorSum([213,412], [-4,-302]) == [209,110])
assert(vectorSum([2,4,1,2], [-4,-302,2,1]) == 
                 [-2,-298,3,3])
###################################################
def dotProduct(a,b):
    length = min(len(a), len(b))
    i = 0
    total = 0
    while (i < length):
        total = total + a[i] * b[i]
        i += 1
    return total

assert(dotProduct([1,2,3], [4,5,6]) == 32)
assert(dotProduct([2,4], [20,30]) == 40 + 120)
###################################################
def isRotation(a1, a2):
    i = 0
    while (i < len(a1)):
        if (a1 == a2):
            return True
        else:
            a1.append(a1[0])
            a1.pop(0)
            # print(a1)
            i += 1
    return False

assert(isRotation([2,3,4,5,6], [2,3,4,5,6]) == True)
assert(isRotation([2,3,4,5,6], [3,4,5,6,2]) == True)
assert(isRotation([2,3,4,5,6], [4,5,6,2,3]) == True)
assert(isRotation([2,3,4,5,6], [5,6,2,3,4]) == True)
assert(isRotation([2,3,4,5,6], [5,6,2,3,5]) == False)
assert(isRotation([2,3,4,5,6], [6,2,3,4,5]) == True)

###################################################
def nondestructiveRotateList(a, n):
    i = 0
    b = a + []
    if (n >= 0):    
        while (i < n):
            b = [b[len(b) - 1]] + b[:(len(b) - 1)]
            i += 1
    else:
        n = abs(n)
        while (i < n):
            b = b[1:] + [b[0]]
            i += 1
    return b

assert(nondestructiveRotateList([1,2,3,4], 1) == [4,1,2,3])
assert(nondestructiveRotateList([4,3,2,6,5], 2) == [6, 5, 4, 3, 2])
assert(nondestructiveRotateList([1,2,3], 0) == [1,2,3])
assert(nondestructiveRotateList([1, 2, 3], -1) == [2, 3, 1])

###################################################
def destructiveRotateList(a, n):
    i = 0
    if (n >= 0):    
        while (i < n):
            a.insert(0, a[len(a) - 1])
            a.pop(len(a) - 1)
            i += 1
    else:
        n = abs(n)
        while (i < n):
            a.append(a[0])
            a.pop(0)
            i += 1

a = [4,3,2,6,5]# [1,2,3,4]
destructiveRotateList(a,-2)
print(a)

b = nondestructiveRotateList([4,3,2,6,5], -2)
print(b)
assert(a == b)

###################################################
def moveToBack(a, b):
    j = 0
    while (j < len(b)):
        i = 0
        count = 0
        while (i < len(a)):
            count_a = a.count(a[i])
            if (b[j] == a[i]):
                a.append(a[i])
                a.pop(i)
                count += 1
                if (count >= count_a):
                    break
            else:
                i += 1
            
        j += 1

a = [2, 3, 3, 4, 1, 5]
moveToBack(a, [3])
assert(a == [2, 4, 1, 5, 3, 3])

a = [2, 3, 3, 4, 1, 5]
moveToBack(a, [2, 3])
assert(a == [4, 1, 5, 2, 3, 3])

a = [2, 3, 3, 4, 1, 5]
moveToBack(a, [3, 2])
assert(a == [4, 1, 5, 3, 3, 2])
#################################################
def binaryListToDecmial(a):
    i = 0
    output = 0
    while (i < len(a)):
        output = output + a[i] * (2 ** (len(a) - i - 1))
        i += 1
    return output

assert(binaryListToDecmial([1, 0]) == 2)
assert(binaryListToDecmial([1, 0, 1, 1]) == 11) 
assert(binaryListToDecmial([1, 1, 0, 1]) == 13)

#################################################
def split(s, delimiter):
    i = 0
    output = []
    tmp = ""
    while (i < len(s)):
        if (s[i] != delimiter):
            tmp = tmp + s[i]
        else:
            output = output + [tmp]
            tmp = ""
        i += 1
    output = output + [tmp]
    return output

assert(split("ab,cd,efg", ",") == ["ab", "cd", "efg"])
assert(split("a,b,c,d,e,f,g", ",") == ["a","b","c","d","e","f","g"])

#################################################
def join(L, delimiter):
    i = 0
    output = ""
    while (i < len(L)):
        j = 0
        while (j < len(L[i])):
            if (L[i][j] != delimiter):
                output = output + L[i][j] 
            j += 1
        i += 1
        if (i < len(L)):
            output = output + delimiter
    return output

assert("ab,cd,efg" == join(["ab", "cd", "efg"], ","))
assert("a,b,c,d,e,f,g" == join(["a","b","c","d","e","f","g"], ","))
