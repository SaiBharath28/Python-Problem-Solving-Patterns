# Example input string
s = "a1b2"

# Step 1: Initialize the result list with an empty string (starting point)
result = ['']

# Step 2: Loop through each character of the string
for char in s:
    # Create a new list to store new permutations for this character
    new_result = []

    # Step 3: For each string in result, add both lowercase and uppercase of the current character
    for subset in result:
        if char.isalpha():  # Only change case for alphabetic characters
            new_result.append(subset + char.lower())  # Add lowercase version
            new_result.append(subset + char.upper())  # Add uppercase version
        else:
            new_result.append(subset + char)  # Non-alphabetic characters stay the same

    # Step 4: Update result with the new permutations
    result = new_result

# Step 5: Print the result
print(result)
