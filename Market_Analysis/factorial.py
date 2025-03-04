def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")
