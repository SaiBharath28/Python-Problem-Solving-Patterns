s1 = "cbaebabacd"
s2 = "abc"
n = len(s1)
m = len(s2)
ans = []
left = 0
dici = {}

# Frequency map for characters in s2
for char in s2:
    if char in dici:
        dici[char] += 1
    else:
        dici[char] = 1

# Initialize count of distinct characters
count = len(dici)

for right in range(n):
    # Add character to the dictionary (window expand)
    if s1[right] in dici:
        dici[s1[right]] -= 1
        if dici[s1[right]] == 0:
            count -= 1

    # Shrink window if we have more than m characters
    if right - left + 1 > m:
        if s1[left] in dici:
            dici[s1[left]] += 1
            if dici[s1[left]] == 1:
                count += 1
        left += 1  # Move left pointer

    # If all characters' frequency matches, it's an anagram
    if right - left + 1 == m and count == 0:
        ans.append(left)

print(ans)  # Output: [0, 6] (Indices where "abc" anagrams are located)
