import heapq  # Min-Heap

# Example input
lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Step 1: Create an empty heap
min_heap = []

# Step 2: Insert the first element of each list into the heap
for i in range(len(lists)):
    if lists[i]:  # Check if the list is not empty
        heapq.heappush(min_heap, (lists[i][0], i, 0))  # (value, list index, element index)

# Step 3: Process the heap to merge lists
result = []

while min_heap:
    value, list_index, elem_index = heapq.heappop(min_heap)
    result.append(value)

    # Step 4: Add the next element from the same list
    if elem_index + 1 < len(lists[list_index]):
        next_value = lists[list_index][elem_index + 1]
        heapq.heappush(min_heap, (next_value, list_index, elem_index + 1))

print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
