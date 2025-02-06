arr = [3, 4, -1, 1]  # Example input
n = len(arr)

# Step 1: Apply Cyclic Sort
i = 0
while i < n:
    correct_index = arr[i] - 1  # The number should be at index (num - 1)
    if 1 <= arr[i] <= n and arr[i] != arr[correct_index]:  # Swap if misplaced
        arr[i], arr[correct_index] = arr[correct_index], arr[i]
    else:
        i += 1  # Move to the next index

# Step 2: Find the Smallest Missing Positive Number
smallest_missing = n + 1  # Default in case all numbers are correct
for i in range(n):
    if arr[i] != i + 1:
        smallest_missing = i + 1
        break

print(smallest_missing)  # Output: 2
