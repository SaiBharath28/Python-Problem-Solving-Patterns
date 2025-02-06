arr = [2, -1, 1, 2, 2]

# Base case: Array length less than 1 or invalid case
if not arr or len(arr) == 1:
    print(False)  # No cycle if the array is empty or has just one element.
else:
    n = len(arr)  # Length of the array
    slow = 0  # Initialize slow pointer at index 0
    fast = 0  # Initialize fast pointer at index 0

    # Iterate to find the cycle
    while True:
        # Move slow pointer one step ahead
        slow = (slow + arr[slow]) % n
        # Move fast pointer two steps ahead
        fast = (fast + arr[fast]) % n
        fast = (fast + arr[fast]) % n

        # If slow and fast pointers meet, cycle is detected
        if slow == fast:
            print(True)
            break

        # If slow and fast pointers move in opposite directions or out of bounds, no cycle
        if arr[slow] * arr[fast] <= 0:
            print(False)
            break
