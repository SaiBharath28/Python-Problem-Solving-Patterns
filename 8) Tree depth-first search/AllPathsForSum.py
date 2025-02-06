# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node's value
        self.left = left  # Left child
        self.right = right  # Right child


# Function to find all paths for the given sum
def allPathsForSum(root, target_sum):
    # List to store all valid paths
    result = []

    # Helper function to perform DFS
    def dfs(node, current_sum, path):
        # Base case: if the node is None, return
        if not node:
            return

        # Add the current node's value to the path
        path.append(node.val)

        # If it's a leaf node (no children) and the path sum equals target_sum
        if not node.left and not node.right and current_sum + node.val == target_sum:
            result.append(list(path))  # Add the path to result

        # Recur for the left and right subtrees
        dfs(node.left, current_sum + node.val, path)
        dfs(node.right, current_sum + node.val, path)

        # Backtrack: remove the current node from path to explore other paths
        path.pop()

    # Start the DFS with initial sum 0 and empty path
    dfs(root, 0, [])

    return result


# Example usage:

# Create the binary tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

# Set the target sum
target_sum = 22

# Call the function
print(allPathsForSum(root, target_sum))
