l = [5, 9, 1, 8, 7]
n = len(l)
left = 0
temp = 0
result = 0
k = 3  # Window size

for right in range(n):
    temp += l[right]  # Add new element to the window

    if right - left + 1 > k:  # Ensure window size remains 'k'
        temp -= l[left]  # Remove the leftmost element
        left += 1  # Move the left pointer

    if right - left + 1 == k:  # When window size is 'k', check max sum
        result = max(result, temp)


print(result)
