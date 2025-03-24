# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next
# #Go through each node
# #compare nodes, if gretaer, change to new node, else procede
# def find_max(head):
#     cur, max_val = head, 0
#     while cur:
#         if cur.value > max_val:
#             max_val = cur.value
#         cur = cur.next

#     return max_val


# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
#         #           c
#         # max = self.head
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))


'''
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
    #Isabelle -> Alfonso -> Cyd
    #                c             n 
    current = head
    while current.next:
        if current.next.next == None:
            break
        current = current.next

    current.next = None 
    return head



head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))
'''


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

#create a set
#go through the nodes
#if node is in set, ignore and move to the next node
#return the head of the linked list 

#1 -> 2 -> 3 -> 3 -> 4 -> 5
# c   cn   n
# c.next = n
# cn = cn.next
# n = n.next

#while c.next
#if c.next.value in cont
#c.next = c.next.next
#c = c.next.next
#continue
# def delete_dupes(head):
#     container_ = set()
#     cur = head
#     while cur.next:
#         container_.add(cur.value)
#         if cur.next.value in container_:
#             cur.next = cur.next.next
#             cur = cur.next.next
#             continue
#         else:
#             cur = cur.next
#     return head


# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))


'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list where ListNode.val == val. Return the head of the modified list.

Example 1:
Input:

Linked List: 1 → 2 → 6 → 3 → 4 → 5 → 6

Value to Remove: 6

Output:

Modified Linked List: 1 → 2 → 3 → 4 → 5

Explanation:

The nodes with value 6 are removed from the list. Initially, the list is 1 → 2 → 6 → 3 → 4 → 5 → 6.

After removing all nodes with 6, the resulting linked list is 1 → 2 → 3 → 4 → 5.
'''

# def remove_elements(head, val):
#     dummy = ListNode(0)         # Create a dummy node
#     dummy.next = head           # Point dummy's next to the original head
#     current = dummy             # Start traversal from dummy

#     while current.next:
#         if current.next.val == val:
#             current.next = current.next.next  # Skip the node with the value
#         else:
#             current = current.next            # Move to next node

#     return dummy.next  # Return the new head (which may have changed)


'''
Write a function merge_two_lists(l1, l2) merges two sorted linked lists l1 and l2 returns the head of the merged and sorted linked list.

Input:
l1: The head of the first sorted linked list.

l2: The head of the second sorted linked list.

Output:
Returns the head of a merged and sorted linked list.

Example 1:

Input:
l1 = create_linked_list([1, 3, 5]) 
l2 = create_linked_list([2, 4, 6])

Output:
merged_list = merge_two_lists(l1, l2) 
# The linked list should represent [1, 2, 3, 4, 5, 6]
'''

# def merge_two_lists(l1, l2):
#     dummy = SinglyLinkedListNode(0)  # Dummy node to simplify logic
#     current = dummy

#     while l1 and l2:
#         if l1.data < l2.data:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next

#     # Attach the remaining part
#     if l1:
#         current.next = l1
#     elif l2:
#         current.next = l2

#     return dummy.next  # The merged list starts at dummy.next


'''
Given the head of a singly linked list, return True if the node values form a palindrome and False otherwise.

A palindrome is a sequence that reads the same forward and backward.

Example 1: Palindrome List
Input:

Linked list: 1 → 2 → 2 → 1

Output:

True

Explanation:

The linked list reads the same forward (1 → 2 → 2 → 1) and backward (1 → 2 → 2 → 1), so it is a palindrome.
'''

# def is_palindrome(head):
#     if not head or not head.next:
#         return True

#     # Step 1: Find the middle using fast and slow pointers
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     # Step 2: Reverse the second half
#     prev = None
#     while slow:
#         next_node = slow.next
#         slow.next = prev
#         prev = slow
#         slow = next_node

#     # Step 3: Compare first half with reversed second half
#     left = head
#     right = prev
#     while right:
#         if left.data != right.data:
#             return False
#         left = left.next
#         right = right.next

#     return True