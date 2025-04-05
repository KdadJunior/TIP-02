'''
Given the head of a 1-indexed singly linked list, write a function odd_even_list()
that groups all the nodes with odd indices together followed by the nodes with even indices,
and return the head of the modified list.
The first node in the input list is considered odd indexed, the second node is even indexed, and so on.
The relative order inside both the even and odd groups should remain as it was in the input.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''
# def odd_even_list(head):
#     if not head or not head.next:
#         return head

#     odd = head
#     even = head.next
#     even_head = even

#     while even and even.next:
#         odd.next = even.next
#         odd = odd.next

#         even.next = odd.next
#         even = even.next

#     odd.next = even_head
#     return head

'''
Given a Circular Linked List node, which is sorted in non-descending order,
write a function to insert a new node with value insert_val into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.
If the list is empty (i.e., the given node is None), you should create a new single circular list and return the reference to that single node.
Otherwise, you should return the originally given node.

Example 1:
Input: head = 3 -> 4 -> 1 (circular), insert_val = 2  
Output: 3 -> 4 -> 1 -> 2 (still circular)

Example 2:
Input: head = None, insert_val = 1  
Output: 1 (single circular node)

Example 3:
Input: head = 1 (self-looped), insert_val = 0  
Output: 1 -> 0 (circular)
'''

# def insert_into_sorted_circular_list(head, insert_val):
#     new_node = ListNode(insert_val)

#     # Case 1: List is empty
#     if not head:
#         new_node.next = new_node
#         return new_node

#     prev, curr = head, head.next
#     inserted = False

#     while True:
#         # Case 2: Normal insert between two nodes
#         if prev.val <= insert_val <= curr.val:
#             inserted = True

#         # Case 3: Wrap around point (max -> min)
#         elif prev.val > curr.val and (insert_val >= prev.val or insert_val <= curr.val):
#             inserted = True

#         if inserted:
#             prev.next = new_node
#             new_node.next = curr
#             return head

#         prev, curr = curr, curr.next

#         # Came full circle without inserting
#         if prev == head:
#             break

#     # Case 4: All nodes have same value or insert_val doesn't fit above
#     prev.next = new_node
#     new_node.next = curr
#     return head
