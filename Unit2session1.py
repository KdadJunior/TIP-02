#PLAN
#Loop through values of dictionary
#Add up the values and return

'''
def total_treasure(treasure_map):
    total = 0
    for num in treasure_map.values()
        total += num
    return total
'''


#PLAN
#Create an empty dictionary 
#Loop through the message, add to dictionary and set values
#if length of dictionary is less than 26, return False
#else return True

'''
def can_trust_message(message):
    m_dict = {}
    for alph in message:
        if alph in m_dict:
            m_dict[alph] += 1
        else:
            m_dict[alph] = 1
    if len(m_dict) < 26:
        return False
    return True


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
'''


#PLAN
#Create a duplicate array
#Create empty dict
#Loop through arr, add to dict and set value
#As you add, if num is already in dict and not presesent in duplicate array, append num to duplicate aray

'''
def find_duplicate_chests(chests):
    duplicates_arr = []
    chest_dict = {}
    for num in chests:
        if num in chest_dict:
            chest_dict[num] += 1
            if num not in duplicates_arr:
                duplicates_arr.append(num)
        else:
            chest_dict[num] = 1
    return duplicates_arr

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
'''

#PLAN
#from collections mport Counter to create a dict of elements and their frequencies 
#Create a list of the frequencies returned as dict.values()
#sort the list, so as to take care of two scenarios
#Scenario 1: All frequencies are the same except one character with frequency 1
#Scenario 2: All frequencies are the same except one character with frequency one more than the others

'''
def is_balanced(code):
    from collections import Counter
    freq = Counter(code)
    counts = list(freq.values())
    counts.sort()
    #Scenario 1
    if counts[0] == 1:
        all_same = True
        for count in counts[1:]:
            if count != counts[1]:
                all_same = False
                break
        if all_same:
            return True
    #Scenario 2
    counts[-1] -= 1
    all_same = True
    for count in counts:
        if count != counts[0]:
            all_same = False
            break
    if all_same:
        return True
    return False

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2))
'''