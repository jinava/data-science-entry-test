def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    
    # Validate that input is a list
    if not isinstance(lst, list):
        return f"Error: Input must be a list, got {type(lst)}"
    
    # Initialize index, and use while loop to iterate through the list
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]  # Found first negative number
        index += 1

    # If loop completes without finding a negative number   
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print("\n=== Q6: Task 2 Test Scenarios ===\n")

# Define test cases
test_cases = [
    [3, 5, -1, 7, -2, 8],
    [2, 10, 7, 0],
]

for test_num, test_list in enumerate(test_cases, 1):
    print(f"Test Case {test_num}:\n")
    print(f"Input list: {test_list}")

    # Execute the function
    result = find_first_negative(test_list)
    
    print(f"Result: {result}\n")

print("=== Task 2 Complete ===")

