def swap(x, y):
    """
    Task 1
    - Swaps the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric.
    - Print the swapped values if both x and y are numeric.
    """
    
    # Check if both x and y inputs are numbers (int or float).
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # The Swap Logic: The right side (y, x) creates a temporary tuple, 
    # and the left side unpacks it into the variables.
    # Unpacking is a concise way to swap the values of two variables without a temporary variable.
    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

print("\n=== Q1: Task 2 Test Scenarios ===\n")

# Define the test scenarios
test_cases = [("Apple", 10), (9, 17)]

for test_num, (x_val, y_val) in enumerate(test_cases, 1):
    print(f"Test Case {test_num}:\n")
    print(f"Input: x = {x_val}, y = {y_val}")
    
    # Invoke the function
    result = swap(x_val, y_val)
    
    # Handle the error condition
    if result == -1:
        print("Function returned -1 (non-numeric input)")
    print()

print("=== Task 2 Complete ===")