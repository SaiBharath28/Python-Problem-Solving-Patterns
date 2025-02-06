# Initial sorted array
arr = [-9, -7, -3, 2, 4, 8]

n = len(arr)
left = 0
right = n - 1
result = [0] * n  # Array to store the squared results
index = n - 1  # We will fill the result array from the end

# Using two-pointer approach
while left <= right:
    # Square the elements at the left and right pointers
    left_square = arr[left] ** 2
    right_square = arr[right] ** 2

    # Place the larger square in the result array
    if left_square > right_square:
        result[index] = left_square
        left += 1  # Move the left pointer inward
    else:
        result[index] = right_square
        right -= 1  # Move the right pointer inward

    # Move the index of the result array
    index -= 1

# Now, 'result' contains the sorted squares
print(result)
