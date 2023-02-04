import pypeg2 as pp
from textwrap import dedent


# This list has the allowable verbs, and their synonyms. The terminal (no synonym) must be here too for the system
# to recognise it as a verb
verb_synonyms = {
    ("walk",): "walk",
    ("go",): "walk",
    ("run",): "walk",
    ("move",): "walk",

    ("hit",): "hit",
    ("punch",): "hit",

    ("take",): "take",
    ("get",): "take",
    ("pick", "up"): "take",

    ("lift",): "lift",

    ("use",): "use",
    ("try",): "use",

    ("inspect",): "inspect",
    ("look", "at"): "inspect",

    ("climb",): "climb",
    ("climb", "up"): "climb",

    ("open",): "open",
    ("unlock",): "open"
}

class Verb(tuple):
    verbs = verb_synonyms.keys()
    grammar = pp.Enum(verbs)

noun_synonyms = {
    ("back",):                  ("backward",),
    ("backwards",):             ("backward",),    
    ("forwards",):              ("forward",),
    ("unidentified", "plant"):  ("plant", "pot"),
    ("withered", "plant"):      ("plant", "pot"),
    ("pot",):                   ("plant", "pot"),
    ("plant",):                 ("plant", "pot"),
}

class Noun(tuple):
   grammar = pp.some(pp.word)

class Filler(str):
    grammar = ["the", "a", "an"]

class Answer(list):
    grammar = [
        (pp.attr('verb', Verb),), # Verb only
        (pp.attr('verb', Verb), pp.optional(Filler), pp.optional(pp.attr('noun', Noun))), # Verb and some nouns
        (pp.attr('noun', Noun),) # Noun only
    ]

def add_exit(location, direction, exit_location):
    location['exits'][direction] = exit_location

def check_door_key(player):
    if "iron_key" in player.items:
        print("You unlock the door with the iron key")
        add_exit(rooms['front_door'], "forward", "lobby")
    else:
        print("The door is very solid and locked.")

rooms = {
    "path": {
        "description": """\
            You are on the path to the big spooky mansion.
            Either side of you are two large bushy trees.

            In front of you is the way to the front door.
        """,
        "exits": {
            "forward": "front_door",
            # "backward": "run_away"
        },
        "synonyms": {
            ("trees",):                     ("tree",),
            ("bushy", "trees"):             ("tree",),
            ("bushy", "tree"):              ("tree",),
            ("large", "tree"):              ("tree",),
            ("large", "trees"):             ("tree",),
            ("large", "bushy", "tree"):     ("tree",),
            ("large", "bushy", "trees"):    ("tree",),
        },
        "props": {
            ("tree",): {
                "inspect":  {"say": "The tree is made of wood, has rough bark, and has seen better days."},
                "kick":     {"say": "Now your foot hurts. As if to taunt you, the tree sways in the wind a bit."},
                "hit":      {"say": "Now your hand hurts. A slightly angry bird twitters at you and flies off."},
                "climb":    {
                    "say": """\
                        You attempt to climb a tree. You make a poor choice of branches,
                        and a branch near the top comes off.

                        You are not a monkey. You have fallen to your death
                    """,
                    "game_over": True
                }
            }
        }
    },
    "front_door": {
        "description": """\
            You are standing at the front door of the mansion.
            The door is made of dark brown wood, bound in black wrought iron.
            It looks very solid.
            
            Set in the door is a Gargoyle holding a knocker - in iron,
            A decorative letterbox - in iron,
            and a big keyhole - also, you guessed it, in iron.

            To the left of you is a plant pot with a rather withered and
            unidentifiable plant. It smells a bit rotten.
        """,
        "exits": {
            "backward": "path",
            "left": "left_grass",
            "right": "right_grass",
            "forward":"lobby"
            #"pick up unidentifiable plant": print "you see a rustty old black thing.It is a key!"
        },
        "synonyms": {
            ("unidentified", "plant"):  ("plant", "pot"),
            ("withered", "plant"):      ("plant", "pot"),
            ("pot",):                   ("plant", "pot"),
            ("plant",):                 ("plant", "pot"),
            ("gargoyle",):              ("knocker",),
        },
        "props": {
            ("plant", "pot"): {
                "inspect": {"say": """\
                    The plant pot has a withered unidentifiable rotten plant in it. 
                    It looks like there's something underneath it.
                """},
                "lift": {
                    "say": """As you lift the pot, you see a black iron key under it. You decide to pick up the key""",
                    "add_item": "iron_key"
                },
                "take": {
                    "say": """You can't really take the pot, but as you lift it, you find a black iron key and keep that.""",
                    "add_item": "iron_key"
                },
                "kick": {
                    "say": """Well now the plant looks even worse than it did before. It does look like something is under the pot"""
                },
                "kick": {
                    "say": """Well now the plant looks even worse than it did before. It does look like something is under the pot"""
                }
            },
            ("door",): {
                "kick": {
                    "say": "You clutch your foot in pain. The very solid door doesn't even look grazed. "
                },
                "use": {
                    "callback": check_door_key
                },
                "open": {
                    "callback": check_door_key
                },
                "hit": {
                    "say": "Your hand hurts. This door is very solid. The door hasn't budged at all"
                }
            }
        }
        # "actions": {
        #     "kick": {
        #         "door": "That hurts",
        #         "Gargole": "He grumbles",
        #         "Lock": "it's too high",
        #         "Letterbox": "Your foot is now sore",
                
        #     }
        # }
    },
    "left_grass": {
        "description": """
            There is wiry jungle of weeds underfoot.
            As you walk through, rustling reveals things with a few too many legs scurrying away.

            In front of you are spiky thorn bushes, vaguely covering
            the murky windows of the mansion. You cannot see much through the
            window.
        
            There is a large, dishevelled brick wall at the left of the garden.
            You can go back to the front door to the right.
        """,
        "exits": {
            "right": "front_door"
        }
    },
    "right_grass": {
        "description": """
            There is long uncut yellowed grass every where.
            In front of you are spiky thorn bushes, vaguely covering
            the murky windows of the mansion. You cannot see much through the
            window.
        
            A row of creaking, menacing trees marks the right wall of the garden.
            You can go back to the front door to the left.
        """,
        "exits": {
            "left": "front_door"
        }
    },
    "lobby": {
        "description": """\
            You are in a spacious lobby. Either side of you is a grand sweeping staircase meeting in the middle above a 
            very grand looking doorway.

            There is a coat and hat stand with a tattered umbrella lodged in it.

            There are doors to the left and right. The door to the right has the word "staff" above it.
            You can go backwards to use the front door to leave the mansion.

            You hear the wind howling, and feel you should conclude your business with this place soon...
        """,
        "exits": {
            "backward": "front_door",
            "up": "upstairs",
            "forward": "dining_room",
            "left": "study",
            "right": "kitchen",
        }
    },
    "kitchen": {
        "description": """\
            You are in a large kitchen, which looks like it has once been well staffed.
            There are large functional metal appliances and storage, and huge pans.
            There is a distinct lack of food here.

            On one of the counters is a torch.
            Hanging among the utensils is a sharp knife.

            You can go back to the lobby,
            To the left are double swing doors - a service door.
        """,
        "exits": {
            "backward": "lobby",
            "left": "dining_room",
        }
    },
    "study": {
        "description": """\
            You are in a study. The walls are panel lined, with dusty bookshelves in front.
            At the far end of the study is a desk.

            You can go right, back to the lobby.
        """,
        "exits": {
            "forward": "secret_room",
            "right": "lobby"
        }
    },
    "dining_room": {
        "description": """\
            This may one have been a lavish dining room. The great windows have molering curtains across them, letting
            in only a murky brown light. There is a large oak table, with 7 chairs - including one larger pronounced
            chair at the head of the table. 

            There appears to be something served in the middle of the table.

            There is a grand door to the back of the room,
            and a functional double door to the right.
        """
    },
    "upstairs": {
        "description": """\
            You are on the landing at the top of grand sweeping stairs in a spacious lobby.
            
            There is a musty smell and noises strange enough to make you shiver and twitch.

            The rooms up here look much darker.
            You can see doors forward, to the left and to the right of you.

        """,
        "exits": {
            "down": "lobby",
            "forward": "bedroom",
            "left": "lavatory",
            "right": "laboratory"
        }
    },
    "bedroom": {
        "description": """\
            You are in a bedroom with a large four poster bed. There are some disconcerting looking
            lumps in the bed.

            There are some drawers and a dolls house that looks like a an eerie representation of the house you
            are standing in.

            You can go backward to the top of the stairs.
        """,
        "exits": {
            "backward": "upstairs"
        }
    },
    "lavatory": {
        "description": """\
            It is very dark in here. Something large and hairy looms over you ,
            and you feel large arms wrap around you and lift you.

            You have been eaten!
        """,
        "game_over": True
    },
    "laboratory": {},
    "secret_room": {}
}


def game_over():
    print(dedent("""\
        -------------------------------------------------------------------------------
                                Game Over!
        -------------------------------------------------------------------------------
    """))


def main():
    print(dedent("""\
        -------------------------------------------------------------------------------
                                SPOOKY MANSION!
        -------------------------------------------------------------------------------
        You are an adventurer, standing at the path to a large, spooky looking mansion.
        The whereabouts of the owner is unknown. 
        Rumour has it that there is a great treasure, and a dark secret in this mansion.
        """)
    )
    room = rooms["path"]
    inventory = {}
    
    while True:
        print(dedent(room["description"]))
        if room.get("game_over"):
            game_over()
            return

        print("What would you like to do?")
        response = input("> ")

        try:
            parsed = pp.parse(response, Answer)
            print("Verb", repr(parsed.verb))
            print("Noun", repr(parsed.noun))
        except:
            print("I don't know how to do that!")
            continue

        # Parsed verb will be a tuple - synonyms will get you a string, or use the only item in the tuple
        verb = verb_synonyms.get(parsed.verb, parsed.verb(0))
        # Nouns remain a tuple - since they can be descriptive.
        noun = noun_synonyms.get(parsed.noun, parsed.noun)

        exits = room["exits"]
        props = room.get("props", {})
        if verb == "run" and noun == "away":
            print("Leaving is probably a good idea, but that's the end of the game. Bye!")
            game_over()
            return
        elif verb in ['run', 'walk', 'go', 'move']:
            if noun in exits:
                room = rooms[exits[noun]]
            else:
                print("Sorry you can't go that way")
        elif verb in exits:
            room = rooms[exits[verb]]
        elif noun in props:
            actions = props.get(noun)
            if actions:
                for_verb = props.get(verb)
                if for_verb:
                    for action in for_verb:
                        action(player)
        else:
            print("Sorry I didn't understand that.")


if __name__ == '__main__':
    main()
