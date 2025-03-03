#SAMPLE
#SAMPLE
#SAMPLE

'''
def intersect(nums1, nums2):
    from collections import Counter
    count_map = Counter(nums1)
    result = []
    for num in nums2:
        if count_map.get(num, 0) > 0:
            result.append(num)
            count_map[num] -= 1
    result.sort()
    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # Output: [4, 9]
'''

#SAMPLE
#SAMPLE
#SAMPLE

'''
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        # Check if the character is already mapped to a different word
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        # Check if the word is already mapped to a different character
        elif word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            # Create new mappings
            char_to_word[char] = word
            word_to_char[word] = char

    return True

# Example Usage:
pattern1 = "abba"
s1 = "dog cat cat dog"
print(wordPattern(pattern1, s1))  # Output: True

pattern2 = "abba"
s2 = "dog cat cat fish"
print(wordPattern(pattern2, s2))  # Output: False
'''

#SAMPLE
#SAMPLE
#SAMPLE

'''
def groupAnagrams(strs):
    from collections import defaultdict
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    # Return the grouped anagrams
    return list(anagram_map.values())

# Example Usage:
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs1))  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

strs2 = [""]
print(groupAnagrams(strs2))  # Output: [[""]]

strs3 = ["a"]
print(groupAnagrams(strs3))  # Output: [["a"]]
'''