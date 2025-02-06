# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to reverse k nodes in the linked list
def reverse_k_nodes(head, k):
    prev, curr = None, head
    count = 0
    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
    return prev, curr  # Return the new head and the next node after the reversed sublist


# Helper function to print the list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

k = 3  # Reverse every 3 elements

# Step 1: Initialize a dummy node
dummy = ListNode(0)
dummy.next = head
prev_group_end = dummy  # This is where we will connect the reversed sublists

# Step 2: Traverse the list in groups of k
while True:
    group_start = prev_group_end.next
    group_end = prev_group_end
    # Move group_end pointer to the end of the current k-sized group
    for _ in range(k):
        group_end = group_end.next
        if not group_end:
            print_list(dummy.next)  # Print the final modified list
            break  # If fewer than k nodes left, break the loop

    # If fewer than k nodes were left, break out of the main loop
    if not group_end:
        break

    # Step 3: Reverse the current k-group
    next_group_start = group_end.next  # Save the node after the current group
    reversed_head, next_group_start = reverse_k_nodes(group_start, k)

    # Step 4: Connect the reversed sublist back to the previous part of the list
    prev_group_end.next = reversed_head
    group_start.next = next_group_start

    # Step 5: Move prev_group_end to the end of the reversed group
    prev_group_end = group_start
