# class SongNode:
# 	def __init__(self, song, artist, next=None):
# 		self.song = song
#         self.artist = artist
# 		self.next = next
# class SongNode:
# 	def __init__(self, song, next=None):
# 		self.song = song
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
		
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# #Example
# print_linked_list(top_hits_2010s)




class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

#create an empty dictionary
#Go through the linkedlist, have artist as key, frequency as value


def get_artist_frequency(playlist):
	freq_map = {}
	current = playlist
	while current:
		artist = current.artist
		if artist in freq_map:
			freq_map[artist] += 1
		else:
			freq_map[artist] = 1
		current = current.next
	return freq_map


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
	

