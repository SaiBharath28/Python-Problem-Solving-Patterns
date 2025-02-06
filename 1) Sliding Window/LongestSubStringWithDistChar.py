li = "aababcabc"
n = len(li)
ans = 0
left = 0
dici = {}
k = 2  # Number of distinct characters
max_length = 0  # To store the maximum length of valid substring

for right in range(n):
    # Add character to dictionary
    if li[right] in dici:
        dici[li[right]] += 1
    else:
        dici[li[right]] = 1

    # Shrink window if distinct character count exceeds k
    while len(dici) > k:
        dici[li[left]] -= 1
        if dici[li[left]] == 0:
            del dici[li[left]]  # Use del instead of pop
        left += 1  # Move left pointer

    # Update max length when valid window is found
    if len(dici) == k:  # Only update when we have exactly 'k' distinct characters
        max_length = max(max_length, right - left + 1)

print(max_length)
