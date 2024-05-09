def calculateFactorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Test the function
result = calculateFactorial(5)
print("Sample Output: result =", result)

