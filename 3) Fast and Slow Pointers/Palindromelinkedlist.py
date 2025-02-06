# Simulating the linked list using a ListNode class for simplicity
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating a simple linked list: 1 -> 2 -> 3 -> 2 -> 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

# Linking the nodes to form the list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Initializing slow and fast pointers
slow = node1
fast = node1

# Step 1: Find the middle of the linked list using slow and fast pointers
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# Step 2: Reverse the second half of the linked list
prev = None
while slow:
    next_node = slow.next
    slow.next = prev
    prev = slow
    slow = next_node

# Step 3: Compare the first half and reversed second half
first_half = node1
second_half = prev
is_palindrome = True

while second_half:
    if first_half.val != second_half.val:
        is_palindrome = False
        break
    first_half = first_half.next
    second_half = second_half.next

# Output the result
if is_palindrome:
    print("Palindrome linked list")
else:
    print("Not a palindrome linked list")
