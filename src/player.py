from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        inventory =  f"{self.name}'s inventory: "

        for i in self.items:
            inventory += f"{i}, "
        return inventory

    def add(self, item):
        return self.items.append(item)

    def delete(self, item):
        return self.items.remove(item)
