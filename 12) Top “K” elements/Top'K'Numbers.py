import heapq  # Import heapq for Min-Heap

# Example input
arr = [3, 1, 5, 12, 2, 11]
K = 3

# Step 1: Create an empty list for the heap
min_heap = []

# Step 2: Add the first K elements to the heap
for i in range(K):
    min_heap.append(arr[i])  # Add elements
heapq.heapify(min_heap)  # Convert list into a Min-Heap

# Step 3: Process the remaining elements
for i in range(K, len(arr)):
    smallest = min_heap[0]  # Get the smallest in heap

    if arr[i] > smallest:  # If current element is larger
        heapq.heappop(min_heap)  # Remove the smallest element
        heapq.heappush(min_heap, arr[i])  # Insert the new larger element

# Step 4: Print the top K largest elements
print(min_heap)  # Output: [5, 11, 12]
