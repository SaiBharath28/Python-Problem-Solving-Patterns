# Simulating the linked list using a ListNode class for simplicity
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating a simple linked list: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Linking the nodes to form the list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a cycle (5 -> 2)

# Initializing slow and fast pointers
slow = node1
fast = node1

# Flag to indicate whether a cycle exists
has_cycle = False

# Traverse the linked list using slow and fast pointers
while fast and fast.next:
    slow = slow.next  # Move slow pointer one step
    fast = fast.next.next  # Move fast pointer two steps

    if slow == fast:  # If slow and fast pointers meet, cycle exists
        has_cycle = True
        break

# Output the result
if has_cycle:
    print("Cycle detected")
else:
    print("No cycle detected")
