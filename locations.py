
endings = ["end_1", "end_2", "end_3"]


starting_location = {
    "name": "Temple Entrance",
    "description": "You are standing at the entrance of an old temple. The door is open, but it looks like nobody has been here in years.",
    "interactions": {        
        "move north": "You walk towards the temple door.",
        "move east": "There is a crack to the east of the temple door.",
        "move south": "You turn back and leave the temple.",
    },
    "routes": {
        "move north": "t_door",
        "move east" : "crack",
        "move south": "end_1"
    }
}


starting_location_2 = {
    "name": "Temple Entrance",
    "description": "You are standing at the entrance of an old temple. The door is open, but it looks like nobody has been here in years.",
    "interactions": {        
        "move north": "You walk towards the temple door.",
        "move east": "There is a crack to the east of the temple door.",
        "move south": "You turn back and leave the temple.",
    },
    "routes": {
        "move north": "t_door_open",
        "move east" : "crack",
        "move south": "end_1"
    }
}


t_door = {
    "name": "Temple door",
    "description": """The Stone door is large with 2 holes in the door and an 
                    engraved warning above the two holes, most of the text is missing but it reads
                    
                    NE__R Str_y from the righ_ __th 
                    
                    The holes are big enough to fit your hand""",
    "interactions": {
        "both": "you stick a hand in both holes",
        "left": "you stick a hand in the left hole.",
        "right": "you stick a hand in the right hole.",
        "move south": "you step back from the temple door"
    },
    "routes": {
        "both": "end_2",
        "left": "end_2",
        "right": "skele_room",
        "move south": "starting_location"
    }
}

t_door_open = {
    "name": "Temple door",
    "description": """The Temple door is open """,
    "interactions": {
        "move north": "you enter the temple",
        "move south": "you step back from the temple door"
        },
    "routes": {
        "move north": "skele_room",
        "move south": "starting_location_2"
    }
}


skele_room = {
    "name": "Skeleton room",
    "description": """the temple door opens up and your arm is fine, you step into a chamber with 
                    two doors, one door has the symbol of the moon and the other door has the symbol of the sun,
                    there is also a skeleton in the cornor of the room, you can swear he's staring at you""",
    "interactions": {
        "moon door": "you enter the moon door",
        "sun door": "you enter the sun door.",
        "skeleton": "you approach the skeleton",
        "move south": "you go outside the temple"
    },
    "routes": {
        "moon door": "moon_door",
        "sun door": "sun_door",
        "skeleton": "skele_joe",
        "move south": "t_door_open"
    }
}

skele_room_2 = {
    "name": "Skeleton room",
    "description": """after you stop talking to skeleton Joe the temple dors slam shut
                        cutting off your escape, the only way forward is through the temple""",
    "interactions": {
        "moon door": "you enter the moon door",
        "sun door": "you enter the sun door.",
        "skeleton": "you approach the skeleton",
        "move south": "you go outside the temple"
    },
    "routes": {
        "moon door": "moon_door",
        "sun door": "sun_door",
        "skeleton": "skele_joe",
        
    }
}


skele_room_3 = {
    "name": "Skeleton room",
    "description": """after you stop talking to skeleton Joe the temple dors slam shut
                        cutting off your escape, the only way forward is through the temple""",
    "interactions": {
        "moon door": "you enter the moon door",
        "sun door": "you enter the sun door.",
        "skeleton": "you approach the skeleton",
        "move south": "you go outside the temple"
    },
    "routes": {
        "moon door": "moon_door",
        "sun door": "sun_door",
        "skeleton": "skele_joe",
        
    }
}





skele_joe = {
    "name": "Skeleton Joe",
    "description": """You approach the skeleton in the corner, when it suddenly springs to life, you get read to run or fight when...
    the skeleton starts speaking
    
    'Greetings traveler I am skeleton Joe, your the first person to visit this place in a thousand hears' 
    i can help you get futher into the temple in exchange for something of yours'
    
    the skeleton offers you a magic torch the wont go out""",
    "interactions": {
        "give gold": "all your gold",
        "give soul": "you offer your soul for the torch",
        "fight": "you try and fight Joe",
        "leave": "you decline Joes offer"
    },
    "routes": {
        "give gold": "skele_room_3",
        "give soul": "skele_room_3",
        "fight": "end_3",
        "leave": "skele_room_2"
    }
}



end_1 = {
        "end": """You leave the temple behind and decide to not explore its secrets."""
        }

end_2 = {
        "end": """You hear the grinding of stone gears and a pressure on your left hand
                the pressure increases quickly, crushing your hand, you scream and pull
                out your arm but there is nothing but a bloody stump left you die in agony 
                as you bleed to death."""
        }

end_3 = {
        "end": """You tried to fight skeleton joe with your bare hands but before you can even touch him 
                your body freezez in place unable to move , Joe reaches for your chest  and casually rips out your heart
                the last thing you remember the evil laugh
                of skeleton Joe"""
        }