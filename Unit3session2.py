# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] 
# then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order. 

'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res_dict = {}
        res_list = []
        for i, str in list2:
            if str in list1:
                j = list1.index(str)
                res_dict[str] = i+j
        for str, num in res_dict.items():
            if num == min(res_dict.values()):
                res_list.append(str)
        return res_list

'''

# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

# Example 3:
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
 
# Constraints:
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.


# 1. Two Sum Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

'''
def two_sum(numbers, target):
    # Check for empty or single-element lists
    if not numbers or len(numbers) < 2:
        return []

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        # Check if indices are still valid before accessing
        if left >= len(numbers) or right >= len(numbers):
            break

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Test case
print(two_sum([2, 7, 11, 15], 9))  # Example case
print(two_sum([], 9))               # Edge case: empty list
print(two_sum([5], 9))              # Edge case: single-element list


'''

# 2. Kth Largest Element in Array
# Given an integer array nums and an integer k, return the kᵗʰ largest element in the array.
# Note that it is the kᵗʰ largest element in the sorted order, not the kᵗʰ distinct element.
# Solve without sorting.
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

'''
import heapq

def find_kth_largest(nums, k):
    # Create a min-heap of size k
    min_heap = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
    
    # The smallest element in the heap is the kth largest element
    return min_heap[0]

# Test cases
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

'''

# 3. Longest Subarray with Absolute Difference Less Than or Equal to Limit
# Given an array of integers nums and an integer limit, return the size of
# the longest non-empty subarray such that the absolute difference between any two elements
# of this subarray is less than or equal to limit.
# Example 1:
# Input: nums = [8, 2, 4, 7], limit = 4
# Output: 2

'''
from collections import deque

def longest_subarray(nums, limit):
    min_deque = deque()
    max_deque = deque()
    left = 0
    max_length = 0
    
    for right in range(len(nums)):
        # Maintain the min_deque
        while min_deque and nums[right] < nums[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(right)
        
        # Maintain the max_deque
        while max_deque and nums[right] > nums[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(right)
        
        # Ensure the current window meets the limit condition
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left += 1
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()
        
        # Update the maximum length of the valid subarray
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print(longest_subarray([8, 2, 4, 7], 4))  # Output: 2
print(longest_subarray([10, 1, 2, 4, 7, 2], 5))  # Output: 4
print(longest_subarray([4, 2, 2, 2, 4, 4, 2, 2], 0))  # Output: 3

'''