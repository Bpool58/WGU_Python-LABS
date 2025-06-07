"""
he Fibonacci sequence begins with 0 and then 1 follows.
All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13.
Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence.
Any negative index values should return -1.

Ex: If the input is:
7
the output is:
fibonacci(7) is 13
"""

def fibonacci(n):
    # First check if n is negative
    if n < 0:
        return -1
    
    # Handle the first two special cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # For all other cases (n >= 2)
    prev2 = 0  # Start with first number (0)
    prev1 = 1  # Start with second number (1)
    
    # Calculate next numbers up to position n.
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return current

# Test the function
n = 7
result = fibonacci(n)
print(f"fibonacci({n}) is {result}")