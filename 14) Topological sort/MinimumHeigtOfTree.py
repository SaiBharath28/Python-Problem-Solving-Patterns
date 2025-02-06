from collections import deque


# Binary tree node structure
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Function to find the minimum height
def min_height(root):
    if not root:
        return 0

    queue = deque([(root, 1)])  # Queue with root node and height
    while queue:
        node, height = queue.popleft()

        # If we reach a leaf node, return its height
        if not node.left and not node.right:
            return height

        # Add left and right children to the queue
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))


# Example tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(min_height(root))  # Output: 2
