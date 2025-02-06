import heapq  # For handling the heap

# Input arrays and K value
nums1 = [9, 8, 2]
nums2 = [6, 3, 1]
K = 3

# Step 1: Create an empty list for heap (since heapq is a Min-Heap, we'll insert negative sums for Max-Heap behavior)
max_heap = []

# Step 2: Loop through the first array (nums1) and the second array (nums2)
for i in range(len(nums1)):  # Loop through each element in nums1
    for j in range(len(nums2)):  # Loop through each element in nums2
        pair_sum = nums1[i] + nums2[j]  # Sum of current pair
        # Step 3: Push the negative of the sum into the heap for max-heap behavior
        heapq.heappush(max_heap, (-pair_sum, nums1[i], nums2[j]))

# Step 4: Extract the top K pairs with the largest sums
result = []  # List to store the result
for _ in range(K):  # We need to get K largest pairs
    if max_heap:
        # Step 5: Pop from heap, retrieve the pair
        _, num1, num2 = heapq.heappop(max_heap)  # Ignore the negative sign of the sum
        result.append((num1, num2))  # Add the pair to the result

# Print the result
print(result)  # Output: [(9, 6), (9, 3), (8, 6)]
