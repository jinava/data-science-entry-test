def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) 
      in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return "Error: lst must be a list"
    
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print("\n=== Q2: Task 2 Test Scenarios ===\n")

test_cases = [
    ([1, 2, 3, 4, 2, 2], 2, 5),
    (["apple", "banana", "apple"], "apple", "orange")
]

for test_num, (lst, find_val, replace_val) in enumerate(test_cases, 1):
    print(f"Test Case {test_num}:\n")
    print(f"List: {lst}, Find: {find_val}, Replace: {replace_val}")
    result = find_and_replace(lst, find_val, replace_val)
    print(f"Result: {result}\n")

print("=== Task 2 Complete ===")