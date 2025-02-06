# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Function to calculate the sum of path numbers
def sumOfPathNumbers(root):
    def dfs(node, current_sum):
        if not node:
            return 0  # If node is None, no path to sum

        current_sum = current_sum * 10 + node.val  # Add the current node value to the path sum

        # If it's a leaf node, return the current sum
        if not node.left and not node.right:
            return current_sum

        # Recursively sum for left and right subtrees
        left_sum = dfs(node.left, current_sum)
        right_sum = dfs(node.right, current_sum)

        # Return the total sum from both subtrees
        return left_sum + right_sum

    return dfs(root, 0)  # Start DFS from the root with initial sum 0

# Example to test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(sumOfPathNumbers(root))  # Output: 522
