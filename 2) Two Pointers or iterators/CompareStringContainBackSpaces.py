s1 = "ab#c"
s2 = "ad#c"

# Initialize two pointers for each string
p1 = len(s1) - 1
p2 = len(s2) - 1

# Process the strings using two pointers
while p1 >= 0 or p2 >= 0:
    # Process the string s1 (left to right)
    backspace_count = 0
    while p1 >= 0 and (s1[p1] == '#' or backspace_count > 0):
        if s1[p1] == '#':
            backspace_count += 1
        else:
            backspace_count -= 1
        p1 -= 1

    # Process the string s2 (left to right)
    backspace_count = 0
    while p2 >= 0 and (s2[p2] == '#' or backspace_count > 0):
        if s2[p2] == '#':
            backspace_count += 1
        else:
            backspace_count -= 1
        p2 -= 1

    # Compare the characters at the current pointers
    if p1 >= 0 and p2 >= 0 and s1[p1] != s2[p2]:
        print(False)  # Output False if characters don't match
        break
    if (p1 >= 0) != (p2 >= 0):  # If only one pointer has reached the end
        print(False)  # Output False if one pointer is ahead
        break
else:
    print(True)  # Output True if the strings match after processing backspaces
