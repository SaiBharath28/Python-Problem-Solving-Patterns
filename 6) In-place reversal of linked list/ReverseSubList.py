# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

left, right = 2, 4  # Reversing from position 2 to 4

# Step 1: Traverse to left-1 node
dummy = ListNode(0)
dummy.next = head
prev = dummy

for _ in range(left - 1):
    prev = prev.next  # Move prev to node before left

# Step 2: Reverse sublist between left and right
curr = prev.next  # Start of sublist
next_node = None

for _ in range(right - left):
    next_node = curr.next
    curr.next = next_node.next
    next_node.next = prev.next
    prev.next = next_node  # Reverse the links

# Step 3: Print the reversed list
temp = dummy.next
while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next
