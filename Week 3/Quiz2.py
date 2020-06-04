
def isPrime(n):
    i = 2
    while (i < n):
        if (n % i == 0):
            return False
        else: 
            i += 1
    return True

def digitCount(n):
    n = abs(n)
    i = 1
    while (n > 0):
        n //= 10 
        i += 1
    return i - 1   

def getnumber(n, i):
    if (i <= digitCount(n)):
        return n // 10 **(i - 1) % 10

def isTenlyPrime(n):
    if (isPrime(n)):
        # sum digits of the number add up to 10
        i = 1
        digitsum = 0
        while (i <= digitCount(n)):
            digitsum = digitsum + getnumber(n, i)
            i += 1
        
        if (digitsum == 10):
            return True
        else: 
            return False   
    else:
        return False

def nthTenlyPrime(n):
    found = 0
    guess = 0 
    while (found <= n):
        if(isTenlyPrime(guess)):
            found += 1
            guess += 1
        else:
            guess += 1
    return guess - 1

for i in range(0,6):
    print(nthTenlyPrime(i))