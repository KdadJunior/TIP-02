'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right

def sum_tree_levels(node):
    def helper(n, depth, level_sums):
        if not n:
            return
        if depth == len(level_sums):
            level_sums.append(0)
        level_sums[depth] += n.value
        helper(n.left_child, depth + 1, level_sums)
        helper(n.right_child, depth + 1, level_sums)

    level_sums = []
    helper(node, 0, level_sums)
    return level_sums

'''



'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right

def max_depth_sum(node):
    def depth_and_sum(n):
        if not n:
            return (0, 0)

        left_depth, left_sum = depth_and_sum(n.left_child)
        right_depth, right_sum = depth_and_sum(n.right_child)

        current_depth = max(left_depth, right_depth) + 1
        current_sum = left_sum + right_sum + n.value

        return (current_depth, current_sum)

    depth, total_sum = depth_and_sum(node)
    return total_sum

'''


'''
def postorder_traversal(root):
    if not root:
        return []

    result = []

    if root.left:
        result += postorder_traversal(root.left)
    if root.right:
        result += postorder_traversal(root.right)

    result.append(root.val)  # Append root last for postorder

    return result

'''


'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mystery_function(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val * 2)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Test Cases
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(mystery_function(root))

'''


'''
Remove Kth Smallest Node
Given the root of a binary search tree (BST) and an integer k, write a function to return 
the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,None,2], k = 1
    3
   / \
  1   4
   \
    2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,None,None,1], k = 3
      5
     / \
    3   6
   / \
  2   4
 /
1
Output: 3

Example 3:
Input: root = [2,1,3], k = 2
  2
 / \
1   3
Output: 2

'''
# def kth_smallest(root, k):
#     def in_order(node):
#         if not node:
#             return []
#         return in_order(node.left) + [node.val] + in_order(node.right)
    
#     return in_order(root)[k - 1]

# ---ALTERNATIVE FAST SOLUTION-----

# def kth_smallest(root, k):
#     count = 0
#     result = None

#     def in_order(node):
#         nonlocal count, result
#         if not node or result is not None:
#             return
#         in_order(node.left)
#         count += 1
#         if count == k:
#             result = node.val
#             return
#         in_order(node.right)
    
#     in_order(root)
#     return result



'''
Given the root of a binary search tree, remove the node with the value val into the tree.
All nodes in the tree are guaranteed to be unique. Return the root of the modified tree.
If you need to replace a parent node with two children, use the in-order successor of that node.
The in-order successor is the node with the smallest value greater than the value of the removed node.

Example 1:
Input: root = [5, 3, 6, 2, 4, None, 7], key = 3
Output: [5, 4, 6, 2, None, None, 7]

Example 2:
Input: root = [5, 3, 6, 2, 4, None, 7], key = 0
Output: [5, 3, 6, 2, 4, None, 7]

Example 3:
Input: root = [], key = 0
Output: []
'''

# def delete_node(root, key):
#     if not root:
#         return None

#     if key < root.val:
#         root.left = delete_node(root.left, key)
#     elif key > root.val:
#         root.right = delete_node(root.right, key)
#     else:
#         # Case 1 & 2: Node with one or no children
#         if not root.left:
#             return root.right
#         if not root.right:
#             return root.left

#         # Case 3: Node with two children — Find in-order successor
#         successor = root.right
#         while successor.left:
#             successor = successor.left

#         # Replace root value with successor value
#         root.val = successor.val

#         # Delete the in-order successor node from right subtree
#         root.right = delete_node(root.right, successor.val)

#     return root



'''
3. Two Sum BST
Given the root of a binary search tree and an integer k, 
return True if there exist two nodes in the BST such that 
the sum of their values is equal to k, and False otherwise.

Example 1:
Input: root = [5, 3, 6, 2, 4, null, 7], k = 9
    5
   / \
  3   6
 / \    \
2   4    7
Output: True
Explanation: 2 + 7 = 9

Example 2:
Input: root = [5, 3, 6, 2, 4, null, 7], k = 28
    5
   / \
  3   6
 / \    \
2   4    7
Output: False
Explanation: There is no pair with sum equal to 28.

Example 3:
Input: root = [2, 1, 3], k = 1
  2
 / \
1   3
Output: False
Explanation: There is no pair with sum equal to 1.
'''

# def find_target(root, k):
#     seen = set()

#     def dfs(node):
#         if not node:
#             return False
#         if (k - node.val) in seen:
#             return True
#         seen.add(node.val)
#         return dfs(node.left) or dfs(node.right)

#     return dfs(root)
