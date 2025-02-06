# Example input array with duplicates
arr = [1, 2, 2]

# Step 1: Sort the array to handle duplicates easily
arr.sort()

# Step 2: Initialize result with an empty subset (starting point)
result = [[]]

# Step 3: Start looping through the sorted array
for i in range(len(arr)):
    # Step 4: If the current number is the same as the previous one,
    # we only add it to the subsets created in the previous iteration
    if i > 0 and arr[i] == arr[i - 1]:
        # This ensures we only add the current element to new subsets that are formed from previous iterations
        start = len(result) // 2
    else:
        # Otherwise, add it to all existing subsets
        start = 0

    # Step 5: Add current number to the subsets generated so far
    for j in range(start, len(result)):
        result.append(result[j] + [arr[i]])

# Step 6: Print the result
print(result)
