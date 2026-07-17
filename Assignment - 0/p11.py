def factorial_recursive(n):
    """Calculates the factorial of a number using recursion."""
    if n < 0:
        return "Factorial does not exist for negative numbers."
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))
