def calculateAverage(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # To avoid division by zero error for an empty list
    return total / count

# Test the function
sample_input = [10, 15, 20, 25]
result = calculateAverage(sample_input)
print("Sample Output:", result)
