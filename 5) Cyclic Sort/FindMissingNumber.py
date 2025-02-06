arr = [3, 0, 1]  # Example input
n = len(arr)

# Step 1: Apply Cyclic Sort
i = 0
while i < n:
    correct_index = arr[i]  # The number should be at index `arr[i]`
    if arr[i] < n and arr[i] != arr[correct_index]:  # Swap if misplaced
        arr[i], arr[correct_index] = arr[correct_index], arr[i]
    else:
        i += 1  # Move to the next index

# Step 2: Find the Missing Number
missing_number = n  # Default to `n` in case all numbers are correct
for i in range(n):
    if arr[i] != i:
        missing_number = i
        break

print(missing_number)  # Output: 2
