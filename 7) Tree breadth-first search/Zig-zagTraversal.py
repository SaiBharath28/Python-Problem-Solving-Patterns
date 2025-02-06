from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to perform zig-zag level order traversal
def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # Queue to store nodes at each level
    left_to_right = True  # Flag to toggle direction at each level

    while queue:
        level = []
        level_size = len(queue)  # Number of nodes at the current level

        for i in range(level_size):
            node = queue.popleft()  # Pop node from the queue
            level.append(node.val)

            # Add children to the queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # If we need to reverse the level order, reverse it
        if not left_to_right:
            level.reverse()

        result.append(level)  # Add the level to the result
        left_to_right = not left_to_right  # Toggle the direction

    return result

# Example to test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(zigzagLevelOrder(root))  # Output: [[1], [3, 2], [4, 5, 6]]
