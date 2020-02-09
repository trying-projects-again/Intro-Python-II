from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# items

items = {
"gameboy": Item("gameboy", "This is a gameboy, probably needs batteries"),
"batteries": Item("batteries", "Oh boy, some batteries!"),
"money": Item("money", "Oh boy $20!"),
"chair": Item("chair", "This is a chair..."),
"blanket": Item("blanket", "Oh look at that, its a blanket!"),
"pillow": Item("pillow", "This is a pillow.")
}


# items to rooms
room["foyer"].add_item(items["gameboy"])
room["overlook"].add_item(items["batteries"])
room["narrow"].add_item(items["chair"])
room["treasure"].add_item(items["money"])
room["outside"].add_item(items["blanket"])
room["outside"].add_item(items["pillow"])


# Make a new player object that is currently in the 'outside' room.
player_name = input('What should I call ya? ==>  ')
new_player = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def getItem():
    item_choice = input('What do you want to do? Ex: get dog: =>  ')
    for i in new_player.current_room.items:
        if item_choice == 'get ' + i.name:
            new_player.add(i)
            new_player.current_room.delete_item(i)
            Item.pick_up(i)
        else:
            print('Option not available')

def dropItem():
    prompt = input("Would you like to drop some things off? Ex: yes or no =>    ")
    if prompt == 'yes':
        drop_item = input('What would you like to drop? Ex: drop sword: =>  ')
        for i in new_player.items:
            if drop_item == 'drop ' + i.name:
                new_player.current_room.add_item(i)
                new_player.delete(i)
                Item.drop(i)
            else:
                print('Try again?')
    elif prompt == 'no':
        print(f'Thats fine {new_player.name}')
    else:
        print('Not a valid choice')


while True:
    cmd = input(f'\n Which direction {player_name}? ==>  ')
    try:
        if cmd == 'q':
            print(f"Thats fine, go home {new_player.name}")
            break
        if cmd == 'n' or cmd == 'e' or cmd == 'w' or cmd == 's':
            direction = f"{cmd}_to"
            if new_player.current_room.__dict__[direction] == None:
                print("\n Dead end \n")
            else:
                new_player.current_room = new_player.current_room.__dict__[direction]
                print(new_player.current_room)
                if len(new_player.current_room.items) >= 1:
                    getItem()
                    print(new_player)
                    if len(new_player.current_room.items) == 0:
                        dropItem()
                        print(new_player)
    except:
        print('invalid command\n')