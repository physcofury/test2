import locations as l
import character as c


current_location = l.starting_location
game_over = False
win_condition = False


def move(direction):
    global current_location
    

    # Check if the direction is valid
    if direction not in current_location['interactions']:
        print("You can't go that way.")
        return

    # Move to the new location
    new_location_name = current_location['routes'][direction]
    if new_location_name in l.endings:
        print(l.__dict__[new_location_name]['end'])
        global game_over; game_over = True
        return
    

    current_location = l.__dict__[new_location_name]
    


def get_input():
    user_input = input("> ").lower()   
    return(user_input)


def display_location(location):
    print(f"{location['name']}\n")
    print(location['description'])
    print("\nInteractions:")

    for interaction, description in location['interactions'].items():
        print(f"- {interaction}: {description}")


def display_inventory():
    print("Inventory:")

    for item, has_item in c.inventory.items():
        if has_item:
            print(f"- {item}")
    print()


def win():
    global win_condition, game_over

    win_condition = True
    game_over = True

    print("Congratulations! You win!")


def lose():
    global game_over

    game_over = True

    print("Game over.")


def take(item_name):
    c.inventory

    #  Check if the item exists in the current location
    if item_name not in current_location['interactions']:
        print("You can't take that.")
        return

    #  Add the item to the inventory
    if c.inventory[item_name] == False:
        c.inventory[item_name] = True
    
    print(f"You took the {item_name}.")


def give(item_name):
    print(item_name)
    c.inventory
    item_name_s = item_name.split()
    item_name_s = item_name_s[1]
    print(item_name_s)
    
    

    if c.inventory[item_name_s] == True:
        c.inventory[item_name_s] = False
    elif c.inventory[item_name_s] == False:
        c.inventory[item_name_s] = True
    elif c.inventory[item_name_s] == int():
        c.inventory[item_name_s] = c.inventory[item_name_s] = 0


    
    print(f"You gave your {item_name}.")



valid_move_commands = ["move north", "move south", "move east", "move west"]


valid_item_names = ["gold", "key", "soul"]
