import heapq

# Heaps initialization
max_heap = []  # For the smaller half (max-heap simulated with negative values)
min_heap = []  # For the larger half

# Stream of numbers
stream = [1, 2, 3]

for num in stream:
    # Step 1: Add number to max-heap (use negative for max-heap)
    heapq.heappush(max_heap, -num)

    # Step 2: Move the largest from max-heap to min-heap if necessary
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # Step 3: Ensure the top of max-heap is smaller than the top of min-heap
    if min_heap and -max_heap[0] > min_heap[0]:
        # Swap the elements between heaps
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)

    # Step 4: Calculate and print the median
    if len(max_heap) > len(min_heap):
        median = -max_heap[0]  # Top of max-heap
    else:
        median = (-max_heap[0] + min_heap[0]) / 2.0  # Average of both heaps' tops

    print("Current median:", median)
