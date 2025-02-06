import heapq  # For Min-Heap

# Example input
arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
K = 2

# Step 1: Count frequency of each number
freq_map = {}

for num in arr:
    if num in freq_map:
        freq_map[num] += 1  # Increase count if number exists
    else:
        freq_map[num] = 1  # First occurrence

# Step 2: Create an empty heap
min_heap = []

# Step 3: Insert first K elements into the heap
count = 0
for num, freq in freq_map.items():
    if count < K:
        heapq.heappush(min_heap, (freq, num))  # Store (frequency, number)
        count += 1
    else:
        smallest = min_heap[0]  # Get the smallest frequency
        if freq > smallest[0]:  # If current frequency is higher
            heapq.heappop(min_heap)  # Remove the smallest frequency
            heapq.heappush(min_heap, (freq, num))  # Add the new number

# Step 4: Extract top K frequent numbers
result = []
for freq, num in min_heap:
    result.append(num)

print(result)  # Output: [1, 4]
