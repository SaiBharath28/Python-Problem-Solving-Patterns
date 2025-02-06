from collections import defaultdict, deque

# Example input: task dependencies
tasks = [[1, 2], [1, 3], [2, 3]]  # Task 1 must be before Task 2, Task 1 before Task 3, Task 2 before Task 3
num_tasks = 3  # Total number of tasks

# Step 1: Create an adjacency list for graph representation and in-degree array
graph = defaultdict(list)
in_degree = [0] * (num_tasks + 1)  # to track number of incoming edges

# Step 2: Build the graph and calculate in-degree of each node
for u, v in tasks:
    graph[u].append(v)
    in_degree[v] += 1

# Step 3: Initialize the queue with nodes that have zero in-degree (no dependencies)
queue = deque([i for i in range(1, num_tasks + 1) if in_degree[i] == 0])

# Step 4: Process the graph
result = []
while queue:
    task = queue.popleft()
    result.append(task)

    for neighbor in graph[task]:
        in_degree[neighbor] -= 1  # Decrease in-degree for dependent tasks
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# Step 5: If result contains all tasks, return the order
if len(result) == num_tasks:
    print(result)  # Output: [1, 2, 3]
else:
    print("No valid topological order (cycle detected).")
