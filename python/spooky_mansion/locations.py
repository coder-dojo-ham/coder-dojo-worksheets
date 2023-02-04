# This should be read only - and read into the map
starting_location = "path"
game_intro_text = """\
    -------------------------------------------------------------------------------
                            SPOOKY MANSION!
    -------------------------------------------------------------------------------
    You are an adventurer, standing at the path to a large, spooky looking mansion.
    The whereabouts of the owner is unknown.
    Rumour has it that there is a great treasure, and a dark secret in this mansion.
"""

location_items = {
    "pocket lint": {
        "inspect": {
            "say": "A bundle of fluff. Not of much use to anybody.",
        },
        "kick": {
            "say": """\
                You carefully put the bundle of fluff down, and try to kick it.
                Not a lot happens. Your pocket still has lint in it.
            """
        },
        "eat": {
            "say": """\
                You take a bit of the fluff, place it in your mouth and start chewing.
                Your teeth feel really bad with a gritty and cottony texture, along
                with a very unsavoury and unidentifiable flavour.

                With disgust, you wander when you last cleaned these clothes...
            """
        }
    }
}

locations = {
    "away": { # Run away location
        "description": """\
            Leaving is probably a good idea, but that's the end of the game. Bye!
        """,
        "game_over": True,
    },
    "path": {
        "description": """\
            You are on the path to the big spooky mansion.
            Either side of you are two large bushy trees.

            In front of you is the way to the front door.
        """,
        "exits": {
            "forward": "front_door",
            "backward": "away"
        },
        "synonyms": {
            "large bushy tree": "tree",
            "large tree":       "tree",
            "bushy tree":       "tree",
        },
        "props": {
            "tree": {
                "inspect":  {"say": "It is a large bushy tree"},
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
            "left": "left_grass",
            "right": "right_grass",
            "backward": "path",
        },
        "items": {
            "iron key": {
                "inspect": {
                    "say": """A large, iron key. Probably for a similarly solid looking door"""
                },
                "eat": {
                    "say": """\
                        It tastes metallic, but you carry on. You decide not to chew it,
                        and to try and swallow it in one go.

                        As you do so, the keys sticks in your throat and chokes you.
                        You have died, choked by an iron key.
                    """,
                    "game_over": True
                }
            }
        },
        "synonyms": {
            "pot": "plant"
        },
        "props": {
            "door": {
                "inspect": {"say": """\
                    The door is made of dark brown wood, bound in black wrought iron.
                    It looks very solid.

                    Set in the door is a Gargoyle holding a knocker - in iron,
                    A decorative letterbox - in iron,
                    and a big keyhole - also, you guessed it, in iron.
                """},
                "kick": {
                    "say": """\
                        You clutch your foot in pain. The very solid door doesn't even look grazed.
                        The Gargoyle looks like he is smirking around that knocker.
                    """
                },
                "hit": {
                    "say": """\
                        You clutch your hand in pain. The very solid door doesn't even look grazed.
                        The Gargoyle looks like he is smirking around that knocker.
                    """
                },
                "open": {
                    "with_item": {
                        "item": "iron key",
                        "say": """You put the iron key in the lock, and the door can be opened""",
                        "add_exit": ("forward", "lobby")
                    },
                    "say": """\
                        You need a key for that
                    """
                },
                "use": {
                    "with_item": {
                        "item": "iron key",
                        "say": """You put the iron key in the lock, and the door can be opened""",
                        "add_exit": ("forward", "lobby")
                    },
                    "say": """\
                        You need a key for that
                    """
                }
            },
            "plant": {
                "inspect": {"say": """\
                    The plant pot has a withered unidentifiable rotten plant in it.
                    It looks like there's something underneath it.
                """},
                "lift": {
                    "say": """As you lift the pot, you see a black iron key under it. You decide to pick up the key""",
                    "add_item": "iron key"
                },
                "take": {
                    "say": """You can't really take the pot, but as you lift it, you find a black iron key and keep that.""",
                    "add_item": "iron key"
                },
            }
        }
    }, # You need to search the pot, and get the keys to unlock the front door.
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
    }, # In the kitchen is the torch - needed to make the monster exit.
    "study": {
        "description": """\
            You are in a study. The walls are panel lined, with dusty bookshelves in front.
            At the far end of the study is a desk.

            You can go right, back to the lobby.
        """,
    }, # in the bookshelf is a loose book, pulling on it reveals the passage to the secret room.
    "dining_room": {
        "description": """\
            This may one have been a lavish dining room. The great windows have molering curtains across them, letting
            in only a murky brown light. There is a large oak table, with 7 chairs - including one larger pronounced
            chair at the head of the table.

            There appears to be something served in the middle of the table.

            There is a grand door to the back of the room,
            and a functional double door to the right.
        """
    }, # In the table there are the keys to the study.
    "upstairs": {
        "description": """\
            You are on the landing at the top of grand sweeping stairs in a spacious lobby.

            There is a musty smell and noises strange enough to make you shiver and twitch.

            The rooms up here look much darker.
            You can see doors forward, to the left and to the right of you.

        """,
    },
    "bedroom": {
        "description": """\
            You are in a bedroom with a large four poster bed. There are some disconcerting looking
            lumps in the bed.

            There are some drawers and a dolls house that looks like a an eerie representation of the house you
            are standing in.

            You can go backward to the top of the stairs.
        """,
    }, # Nothing yet in here.
    "lavatory": {
        "description": """\
            It is very dark in here. Something large and hairy looms over you ,
            and you feel large arms wrap around you and lift you.

            You have been eaten!
        """,
    }, # This is the dark secret - it will shamble off through the window if you have a lamp.
    # if you have the knife or pan - you will try to fight it, but loose.
    "laboratory": {
        "description": """\
            You find yourself in a room full of strange apparatus. Sparks whizz along rods, things bubble away,
            and amid the chaos you see a small safe.
        """
    }, # The safe has the treasure - win condition.
    "secret_room": {
        "description": """\
            The bookshelf slide aside to reveal a downward sloping corridor,
            ending in a small cubicle of rough hewn stone.

            On the floor is a single yellowing bit of curled up paper"""
    } # the paper has the digits for the safe.
}

