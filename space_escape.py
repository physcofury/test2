import locations as l
import backend as b
import character as c


while not b.game_over:
    # Display current location
    b.display_location(b.current_location)

    # Display inventory
    b.display_inventory()

    # Prompt user for input
    user_input = b.get_input()
    split_input = user_input.split()
    # Handle user input
    
    
    

    if split_input[0] == "take" and len(split_input) > 1 and split_input[1] in b.valid_item_names:
        b.take(user_input[1])

    if split_input[0] == "give" and len(split_input) > 1 and split_input[1] in b.valid_item_names:
        if split_input[1] == "soul":
            c.inventory["torch"] = True
        b.give(user_input)
    #elif b.current_location['name'] == "Treasure Room" and "key" in c.inventory and not b.win_condition:
    #    b.win()
    if user_input in b.current_location["interactions"]:       
        b.move(user_input)

    else:
        print("Invalid command.")

# Display ending message
input("\nPress any key to close game")



