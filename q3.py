def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    
    # Check if key already exists in the dictionary
    if key in dct:
        print(f"Key '{key}' already exists with value: {dct[key]}")

    # Update the dictionary 
    # This will either add a new key or update an existing one  
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print("\n=== Q3: Task 2 Test Scenarios ===\n")

# Define test cases as tuples (dictionary, key, value)
test_cases = [({}, "name", "Alice"), ({"age": 25}, "age", 26)]

for test_num, (dct, key, value) in enumerate(test_cases, 1):
    print(f"Test Case {test_num}:\n")
    print(f"Original: {dct}, {key}, {value}")

    # Execute the function
    result = update_dictionary(dct, key, value)
    
    print(f"Updated dictionary: {result}\n")

print("=== Task 2 Complete ===")

