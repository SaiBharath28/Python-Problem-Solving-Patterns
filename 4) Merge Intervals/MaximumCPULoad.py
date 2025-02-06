import heapq  # Min-Heap for tracking active jobs

# Given jobs: [start, end, load]
jobs = [[1, 4, 3], [2, 5, 4], [7, 9, 6]]

# Step 1: Sort jobs based on start time
jobs.sort()

# Step 2: Initialize variables
min_heap = []  # Stores [end_time, load] of active jobs
current_load = 0  # Tracks current CPU load
max_load = 0  # Stores the maximum CPU load

# Step 3: Process each job
for start, end, load in jobs:
    # Remove jobs that finished before the current job starts
    while min_heap and min_heap[0][0] <= start:
        finished_end, finished_load = heapq.heappop(min_heap)
        current_load -= finished_load  # Reduce load since job ended

    # Add current job to heap
    heapq.heappush(min_heap, (end, load))
    current_load += load  # Increase load

    # Update max load if needed
    max_load = max(max_load, current_load)

# Step 4: Print the result
print(max_load)  # Output: 7
