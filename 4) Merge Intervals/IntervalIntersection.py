A = [[1, 5], [10, 14], [16, 18]]
B = [[2, 6], [8, 10], [11, 20]]

i, j = 0, 0  # Pointers for both lists
result = []

while i < len(A) and j < len(B):
    startA, endA = A[i]
    startB, endB = B[j]

    # Find intersection
    start = max(startA, startB)
    end = min(endA, endB)

    if start <= end:  # Valid intersection
        result.append([start, end])

    # Move the pointer that ends first
    if endA < endB:
        i += 1
    else:
        j += 1

print(result)  # Output: [[2, 5], [10, 10], [11, 14], [16, 18]]
