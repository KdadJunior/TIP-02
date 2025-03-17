# def is_valid(s):
#     stack = []
    
#     for char in s:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 return False  # Mismatch or no matching '('
    
#     # Finally, return True only if no unmatched '(' remain
#     return len(stack) == 0


'''
Given an array of integers arr, return True if and only if it is a valid mountain array.

An arr is a mountain array if and only if:

len(arr) >= 3
There exists some i with 0 < i < len(arr) - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[len(arr) - 1]
Example 1
Input: arr = [2, 1]
Output: False

Example 2
Input: arr = [3, 5, 5]
Output: false

Example 3
Input: arr = [0, 3, 2, 1]
Output: true
'''

# def valid_mtn_arr(arr):
#     n = len(arr)
#     # 1) Must have at least 3 elements
#     if n < 3:
#         return False
#     i = 0
#     # 2) Climb strictly upward
#     while i + 1 < n and arr[i] < arr[i + 1]:
#         i += 1
#     # Peak cannot be the first or last index
#     if i == 0 or i == n - 1:
#         return False
#     # 3) Climb strictly downward
#     while i + 1 < n and arr[i] > arr[i + 1]:
#         i += 1
#     # If we've reached the end, it's valid
#     return i == n - 1


# if __name__ == '__main__'


'''
Prompt:

Implement a function prime_frequency_map() that iterates over an m × n integer matrix and returns a frequency map of prime numbers found in the matrix.

A prime number is a number greater than 1 that has no divisors other than 1 and itself.

We have provided a helper function is_prime(n) to you, which accepts an integer n and returns True if n is prime and False otherwise.

Example 1:

Input:

csharp
Copy code
matrix = [
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Output:

yaml
Copy code
{2: 1, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}
Example 2:

Input:

csharp
Copy code
matrix = [
  [4, 6, 8],
  [10, 12, 14]
]
Output:

Copy code
{}
'''

# def prime_frequency_map(matrix):
#     freq = {}
#     for row in matrix:
#         for val in row:
#             if is_prime(val):       # Provided helper function
#                 freq[val] = freq.get(val, 0) + 1
#     return freq


'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will be no input like 3a or 2[4].

Example 1
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''

# def decode_string(s):
#     # Stack will hold pairs of (previous_decoded_string, repeat_count)
#     stack = []
#     current_str = []
#     current_num = 0
    
#     for char in s:
#         if char.isdigit():
#             # Build up the repeat count (could be multiple digits)
#             current_num = current_num * 10 + int(char)
#         elif char == '[':
#             # Push the current context onto the stack
#             stack.append((''.join(current_str), current_num))
#             # Reset for the new bracketed substring
#             current_str = []
#             current_num = 0
#         elif char == ']':
#             # Pop the context and repeat the current substring
#             prev_str, repeat = stack.pop()
#             current_str = list(prev_str + ''.join(current_str) * repeat)
#         else:
#             # It's a regular character; accumulate it
#             current_str.append(char)
    
#     # Join everything at the end
#     return ''.join(current_str)
