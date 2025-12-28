def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
 
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return f"Error: Both inputs must be numeric. Got num={type(num)}, divisor={type(divisor)}"

    if divisor == 0:
        return f"Error: Divisor cannot be zero"
    
    if num % divisor == 0:
        return True
    else:
        return False
    
    
# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print("\n=== Q5: Task 2 Test Scenarios ===\n")

test_cases = [(10, 2), (7, 3)]

for test_num, (num, divisor) in enumerate(test_cases, 1):
    print(f"Test Case {test_num}:\n")
    print(f"Number: {num}, Divisor: {divisor}")
    result = check_divisibility(num, divisor)
    print(f"Result: {result}")
    print()

print("=== Task 2 Complete ===")