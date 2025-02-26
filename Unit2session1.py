'''
#PLAN
#Loop through values of dictionary
#Add up the values and return

def total_treasure(treasure_map):
    total = 0
    '''

#PLAN
#Create an empty dictionary 
#Loop through the message and increment each(value) by 1
#look at the dict.values(), if any value is 0, then return False
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

#Understand
#Input: chest array
#Output: array of duplicates
#PLAN
#Create empty dict
#Loop through arr and add to dict and set value
#

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
    #for key, value in chest_dict.items():
     #   if value > 1:
      #      duplicates_arr.append(key)
    return duplicates_arr

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

#[2, 3]
#[1]
#[]