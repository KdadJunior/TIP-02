# #binary search
# #return true if found, false otherwise

# def find_cruise_length(cruise_lengths, vacation_length):
    # left = 0
    # right = len(cruise_lengths) - 1
    
    # while left <= right:
    #     mid = (right + left) // 2

    #     if cruise_lengths[mid] == vacation_length:
    #         return True

    #     elif cruise_lengths[mid] < vacation_length:
    #         left = mid + 1

    #     else:
    #         right = mid - 1
        
    # return False



# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# #                         l=0           m=5   l=6  m=8  r=10

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


#define function
#cabine is list
#pref deck is int
# def find_cabin_index(cabins, preferred_deck):
#     #max
#     if cabins[-1] < preferred_deck:
#         return len(cabins)
    
#     # elif preferred_deck not in cabins:
#     #     return -1
    
#     elif cabins[0] == preferred_deck:
#         return 0
    
#     elif cabins[0] < preferred_deck:
#         #print("Get smaller")
#         return 1 + find_cabin_index(cabins[1:], preferred_deck)
#     else:
#         return 0

'''
    def find_cabin_index(cabins, preferred_deck):
    left = 0
    right = len(cruise_lengths) - 1
    
    while left <= right:
        mid = (right + left) // 2

        if cruise_lengths[mid] == vacation_length:
            return True

        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1

        else:
            right = mid - 1
        
    return False

print(find_cabin_index([1, 3, 5, 6], 5))
#                       l=0     m   r=
print(find_cabin_index([1, 2, 3, 5, 6], 4))
print(find_cabin_index([1, 3, 5, 6], 7))
'''

# Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise.

# A valid pair of parentheses is defined as ().
# The input string will only contain the characters ( or ).
# Each ( must have a corresponding ), and the parentheses must be correctly nested for the string to be considered valid.

# There are two conditions to check:

# Balance: Every ( must be paired with a ). This means the number of ( should be equal to the number of ).

# Correct Nesting: Parentheses must follow a proper order. For example:

# "()" is valid.

# "(())" is valid (correct nesting).

# "())(" is not valid (incorrect order).

# "(()" is not valid (unbalanced).

# Your solution must be recursive.
# Test Input: "(()))"
# Output: False (extra closing parenthesis)

# Test Input: "(())"
# Output: True (valid nesting)

# Test Input: "()"
# Output: True (a single valid pair)

# Test Input: ")("
# Output: False (incorrect order)

# Test Input: "(()"
# Output: False (unbalanced)

# Test Input: ""
# Output: True (an empty string is a valid nesting)

'''
def is_valid_parens(s):
    def helper(s, index, count):
        if index == len(s):
            return count == 0
        if count < 0:
            return False
        if s[index] == '(':
            return helper(s, index + 1, count + 1)
        elif s[index] == ')':
            return helper(s, index + 1, count - 1)
        else:
            return False

    return helper(s, 0, 0)

'''

# Given the heads of two sorted linked lists, merge them into a single sorted linked list using a recursive approach.

# Example 1:

# Input: l1 = [1, 2, 4], l2 = [1, 3, 4]

# Output: [1, 1, 2, 3, 4, 4]

# Example 2:

# Input: l1 = [], l2 = []

# Output: []

# Example 3:

# Input: l1 = [1], l2 = [0]

# Output: [0, 1]

'''
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_lists(l1, l2):
    # Base cases
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Recursive case
    if l1.data < l2.data:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2

'''

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is:

# (0-indexed).
# For example:
# [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot index 3 and become:
# [4, 5, 6, 7, 0, 1, 2].

# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0

# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3

# Output: -1

# Example 3:

# Input: nums = [1], target = 0

# Output: -1

'''
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # target is in the left half
            else:
                left = mid + 1   # target is in the right half

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # target is in the right half
            else:
                right = mid - 1  # target is in the left half

    return -1  # target not found

'''
