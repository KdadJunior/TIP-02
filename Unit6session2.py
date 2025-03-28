# Write a function to find the middle node of a singly linked list.
# If the linked list has an even number of nodes, return the second middle node.
# Input: head = [1, 2, 3, 4, 5] 
# Output: Node with value 3
# Input: head = [1, 2, 3, 4, 5, 6] 
# Output: Node with value 4


#1 -> 2 -> 3 -> 4 -> 5
#          s
#                    f

#1 -> 2 -> 3 -> 4 -> 5 -> 6
#               s
#                             f

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def findmiddle(Llist):
#     current = Llist
#     slow = current
#     fast = current

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     return slow.val
    
# head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# print(findmiddle(head1))

'''Problem: Merging Two Sorted Linked Lists
You are given the heads of two sorted linked lists. Your task is to merge them into a single sorted linked list and return its head.
Each list is already sorted in ascending order, so the merged list must also maintain this order.
Example:
python
CopyEdit
list1 = 1 -> 3 -> 5
list2 = 2 -> 4 -> 6

merge_sorted(list1, list2)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6'''

#dummy = ListNode(0)
#current = dummy
#l1 = list1
#l2 = list2
#while l1 and l2, if l1.value < l2.value, current.next = l1
#                  current = current,next
#                  if l1.value > l2.value, current.next = l2
#                   current = current.next
#if l1, current.next = l1
#elif l2, current.next = l2


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
#Use two pointer approch
#first and second, second moves through the nodes
#edge case, if no clues, if only one clue, 

def is_circular(clues):
    first = clues
    second = clues

    if not clues:
        return False
    
    if first and (first.next == None):
        return False
	
#1 -> 2 -> 3 -> 1
    while second is not None and second.next is not None:
        first = first.next
        second = second.next.next
        if first == second:
            break
    
    if second is None or second.next is None:
        return False
    
    first = clues
    while first != second:
        first = first.next
        second = second.next
    
    return first == clues

    #while second and second.next != first:
    

#Example

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))


#Output
''' True '''


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def collect_false_evidence(evidence):
#     while second is not None and second.next is not None:
#         first = first.next
#         second = second.next.next
#         if first == second:
#             break
#     if second is None or second.next is None:
#          return False
    
#     first = clues
#     while first != second:
#         first = first.next
#         second = second.next
    
#     return first == clues



# def has_cycle(head):
#     if not head:
#         return False
    
#     slow = head  # Starts at the head
#     fast = head  # Also starts at the head

#     while fast and fast.next:
#         slow = slow.next          # Move slow pointer by one
#         fast = fast.next.next     # Move fast pointer by two

#         if slow == fast:          # If they meet, there's a cycle
#             return True
    
#     return False


# clue1 = Node("Unmarked sedan seen near the crime scene")
# clue2 = Node("The stolen goods are at an abandoned warehouse")
# clue3 = Node("The mayor is accepting bribes")
# clue4 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue4
# clue4.next = clue2

# clue5 = Node("A masked figure was seen fleeing the scene")
# clue6 = Node("Footprints lead to the nearby woods")
# clue7 = Node("A broken window was found at the back")
# clue5.next = clue6
# clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))

# #Output
# '''
# ['The stolen goods are at an abandoned warehouse', 'The mayor is accepting bribes', 
# 'They dumped their disguise in the lake']
# []
# '''