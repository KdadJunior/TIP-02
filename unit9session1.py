# from collections import deque 

# # Tree Node class
# class TreeNode:
#   def __init__(self, value, key=None, left=None, right=None):
#       self.key = key
#       self.val = value
#       self.left = left
#       self.right = right

# def build_tree(values):
#   if not values:
#       return None

#   def get_key_value(item):
#       if isinstance(item, tuple):
#           return item[0], item[1]
#       else:
#           return None, item

#   key, value = get_key_value(values[0])
#   root = TreeNode(value, key)
#   queue = deque([root])
#   index = 1

#   while queue:
#       node = queue.popleft()
#       if index < len(values) and values[index] is not None:
#           left_key, left_value = get_key_value(values[index])
#           node.left = TreeNode(left_value, left_key)
#           queue.append(node.left)
#       index += 1
#       if index < len(values) and values[index] is not None:
#           right_key, right_value = get_key_value(values[index])
#           node.right = TreeNode(right_value, right_key)
#           queue.append(node.right)
#       index += 1

#   return root

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)
      
# def merge_orders(order1, order2):

#     if not order1:
#       return order2
#     if not order2:
#        return order1

#     merged = TreeNode(order1.val + order2.val)

#     merged.left = merge_orders(order1.left, order2.left)
#     merged.right = merge_orders(order1.right, order2.right)

#     return merged

# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)
# print_tree(merge_orders(order1, order2))


# from collections import deque
# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def print_design(design):

#     if not design:
#         return []
    
#     queue = deque([design])
#     result = []

#     while queue:
#         node = queue.popleft()
#         result.append(node.val)

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
    
#     print(result)

# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print_design(croquembouche)

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def max_tiers(cake):
#     # if not cake:
#     #     return 0
    
#     left_height = max_tiers(cake.left)
#     print(left_height)
#     right_height = max_tiers(cake.right)

#     return 1 + max(left_height, right_height)

# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers(cake))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Traversals
def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end=' ')
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.value, end=' ')
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=' ')

# Example tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order Traversal: ")
in_order(root)        # Output: 4 2 5 1 3

print("\nPre-order Traversal: ")
pre_order(root)       # Output: 1 2 4 5 3

print("\nPost-order Traversal: ")
post_order(root)      # Output: 4 5 2 3 1