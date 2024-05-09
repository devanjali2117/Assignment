def listMultiples(n, limit):
    """
    Print the first n multiples of limit.

    Parameters:
    n (int): Number of multiples to print.
    limit (int): The number whose multiples are to be printed.
    """
    multiples = [i * limit for i in range(1, n + 1)]
    print(*multiples)

# Example usage:
listMultiples(3, 5)
