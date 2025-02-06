# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to perform level order traversal
def levelOrder(root):
    if not root:  # If the tree is empty, return an empty list
        return []

    result = []  # This will store the final level order result
    queue = [root]  # Start with the root node in the queue

    while queue:  # Continue until there are no more nodes to process
        level = []  # This list stores nodes at the current level
        level_length = len(queue)  # Number of nodes at the current level

        for i in range(level_length):  # Process all nodes at the current level
            node = queue.pop(0)  # Pop the first node from the queue
            level.append(node.val)  # Add the node value to the level list

            if node.left:  # If the left child exists, add it to the queue
                queue.append(node.left)
            if node.right:  # If the right child exists, add it to the queue
                queue.append(node.right)

        result.append(level)  # Add the current level's nodes to the result

    return result  # Return the result which contains the nodes level by level


# Example to test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(levelOrder(root))  # Output: [[1], [2, 3], [4, 5, 6]]
