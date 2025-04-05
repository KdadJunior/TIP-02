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