def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    # Validate that input s is a string
    if not isinstance(s, str):
        return f"Error: Input must be a string, got {type(s)}"
    
    # Using a loop to build the reversed string
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print("\n=== Q4: Task 2 Test Scenarios ===\n")

# Define test cases
test_cases = ["Hello World", "Python"]

for test_num, test_string in enumerate(test_cases, 1):
    print(f"Test Case {test_num}:\n")
    print(f"Original: '{test_string}'")

    # Execute the function
    result = string_reverse(test_string)
    
    print(f"Reversed: '{result}'\n")

print("=== Task 2 Complete ===")
