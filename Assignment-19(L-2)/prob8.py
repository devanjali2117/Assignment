def findGCD(a, b):
    while b:
        a, b = b, a % b
    return a

gcdResult = findGCD(36, 48)
print("gcdResult =", gcdResult)
