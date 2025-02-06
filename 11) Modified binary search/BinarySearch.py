# Example input
arr = [10, 20, 30, 40, 50]
target = 30

# Step 1: Initialize pointers
low = 0
high = len(arr) - 1

# Step 2: Perform binary search with swapping logic
while low <= high:
    mid = (low + high) // 2  # Find middle index

    if arr[mid] == target:
        print(mid)  # Found target, print index
        break

    if arr[mid] < target:
        # Swap low with mid + 1 (moving towards right)
        low, high = mid + 1, high
    else:
        # Swap high with mid - 1 (moving towards left)
        low, high = low, mid - 1
else:
    print(-1)  # Target not found
