class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.nearby_rooms = []
    
    def set_description(self, description):
        self.description = description
        
    def link_room(self, room, position):
        self.nearby_rooms.append((room, position))

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def move(self, command):
        for room, position in self.nearby_rooms:
            if position == command:
                return room

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for room, position in self.nearby_rooms:
            print(f"The {room.name} is {position}")



class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.message = None
        self.weakness = None
        self.defeated = 0

    def set_conversation(self, message):
        self.message = message

    def talk(self):
        print(f"[{self.name} says]: {self.message}")

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def fight(self, item):
        if item == self.weakness: self.defeated += 1
        return item == self.weakness

    def get_defeated(self):
        return self.defeated

    def set_weakness(self, item):
        self.weakness = item



class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(f"The {self.name} is here - {self.description}")
