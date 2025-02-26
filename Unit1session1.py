# Write a function linear_search() to help Winnie the Pooh locate his lost items.
# The function accepts a list items and a target value as parameters.
# The function should return the first index of target in items, and -1 if target is not in the lst.
# Do not use any built-in functions.

#Note LINEAR SEARCH for unsorted data && when the expected output is in the original order
#Note BINASRY SEARCH for sorted data && when the origianl order does not matter to the output

#PLAN
# USING LINEAR SEARCH FOR MY SOLUTION
#Loop through each elem and compare to target
#return index if target matches 

'''
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print (linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print (linear_search(items, target))
'''


#Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
#bouncy and flouncy both increment the value of the variable tigger by 1.
#trouncy and pouncy both decrement the value of the variable tigger by 1.
#Initially, the value of tigger is 1 because he's the only tigger around!
# Given a list of strings operations containing a list of operations,
# return the final value of tigger after performing all the operations.

#PLAN
#create variable tigger and set to 1
# ++ if bouncy or flouncy
# -- if trouncy or pouncy
'''
def final_value_after_operations(operations):
    tigger = 1
    for word in operations:
        if word == "bouncy" or word == "flouncy":
            tigger += 1
        elif word == "trouncy" or word == "pouncy":
            tigger -= 1

    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print (final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print (final_value_after_operations(operations))
'''

#T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and
# returns a new string that removes any substrings t, i, gg, and er from word.
# The function should be case insensitive.

#Note, string in python is immutable, you can replace but you can not erase
#PLAN
#replace all target characters and strings with '' (empty string)

'''
def tiggerfy(word):
    word = word.lower()
    word = word.replace('t', '')
    word = word.replace('i', '')
    word = word.replace('gg', '')
    word = word.replace('er', '')

    return word

word = "Trigger"
print (tiggerfy(word))

word = "eggplant"
print (tiggerfy(word))

word = "Choir"
print (tiggerfy(word))
'''

#Given an array nums with n integers, write a function non_decreasing()
#that checks if nums could become non-decreasing by modifying at most one element.
#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
# such that (0 <= i <= n - 2).

#PLAN
#I will use count to control number of times we modify
#Loop through nums and compare i <= i+1
#for first violation, we modify the arr and then continue to find second violation

'''
def non_decreasing(nums):
    i = 0
    count = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            count += 1
            if count > 1:
                return False
            if i > 0 and nums[i - 1] > nums[i + 1]:
                nums[i + 1] = nums[i]
            else:
                nums[i] = nums[i + 1]
        i += 1
    return True
    
nums = [4, 2, 3]
print (non_decreasing(nums))

nums = [4, 2, 1]
print (non_decreasing(nums))
'''

#Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day
#and several hidden clues have blown away. Write a function find_missing_clues()
#to help Christopher Robin figure out which clues he needs to remake.
#The function accepts two integers lower and upper and a unique integer array clues.
#All elements in clues are within the inclusive range [lower, upper].
#A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.
#Return the shortest sorted list of ranges that exactly covers all the missing numbers.
#That is, no element of clues is included in any of the ranges, and each missing number is covered by
#one of the ranges.

#PLAN
#function takes (arr, lower, upper)
#sort arr
# I will use the idea of two pointers, first = arr[i=0], second = arr[i+1]
#Check edge case for less than two elements
#I will subtract, second - first = 1 means there's no jump in between, else first++ and --second
#append the arr [first, second]

'''
def find_missing_clues(clues, lower, upper):
    clues.sort()
    result = []
    if len(clues) < 2:
        return result
    for i in range(len(clues) - 1):
        first = clues[i]
        second = clues[i+1]   
        if (second - first) > 1:
            first += 1
            second -= 1
            result.append([first, second])
    if clues[-1] < upper:
        result.append([(clues[-1] + 1),upper])
    return result

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print (find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print (find_missing_clues(clues, lower, upper))
'''

#Rabbit is collecting carrots from his garden to make a feast for Pooh and friends.
#Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that
#are ready to harvest in the vegetable patch. A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.
#Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

#PLAN

def can_place_flowers(flowerbed, n):
    # Write your code here
    count = 0
    for elem in flowerbed:
        if elem == 0:
            count += 1
    if round(count/n) >= 3:
        return True
    return False

flowerbed = [1,0,0,0,0,0,1]
n = 1
print (can_place_flowers(flowerbed, n))