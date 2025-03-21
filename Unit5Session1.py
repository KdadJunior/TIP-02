class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

#of_personality_type takes two argument(townies and personality_type)
#townies(list) and personality_type(string)
#result(list)
#going through townies, if personality_type then append class instance to result
def of_personality_type(townies, personality_type):
    result = []
    for person_object in townies:
        if person_object.personality == personality_type:
            result.append(person_object.name)
    return result



# def message_received(start_villager, target_villager):
#     ptr = start_villager
#     for vil in 


