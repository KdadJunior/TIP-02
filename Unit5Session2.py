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


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

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
def delete_dupes(head):
    container_ = set()
    cur = head
    while cur.next:
        container_.add(cur.value)
        if cur.next.value in container_:
            cur.next = cur.next.next
            cur = cur.next.next
            continue
        else:
            cur = cur.next
    return head


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))