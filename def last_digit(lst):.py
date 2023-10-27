def last_digit(lst):
    if not lst:
        return 1

    result = 1
    for x in reversed(lst):
        # Using modular exponentiation to avoid very large intermediate results
        result = x ** (result if result < 4 else result % 4 + 4)
    
    return result % 10

# Example usage
input_list = [3, 4, 2]
result = last_digit(input_list)
print(result)  # Output: 1