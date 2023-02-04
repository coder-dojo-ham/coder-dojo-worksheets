import pypeg2 as pp
from textwrap import dedent


class Noun(str):
   grammar = pp.word

class Verb(str):
    grammar = pp.word

class Answer(list):
    grammar = pp.attr('verb', Verb), pp.optional(pp.attr('noun', Noun))


def game_over():
    print(dedent("""\
        -------------------------------------------------------------------------------
                                Game Over!
        -------------------------------------------------------------------------------
    """))
    

rooms = {
    "path": {
        "description": """\
            You are on the path to the big spooky mansion.
            Either side of you are two large bushy trees.
            In front of you is the way to the front door.
        """,
        "exits": {
            "forward": "front_door",
            "backward": "run_away"
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
            unidentifiable plant. It smells a bit like a rotten egg!

        """,
        "exits": {
            "backward": "path",
            "left": "left_grass",
            "right": "right_grass",
            #"forward":"lobby"
            #"pick up unidentifiable plant": print "you see a rustty old black thing.It is a key!"
        },
        "actions": {
            "kick": {
                "door": "That hurts",
                "Gargole": "He grumbles",
                "Lock": "it's too high",
                "Letterbox": "Your foot is now sore",
                
            }
        }
    },
    right_grass:{
        "description" """
            There is long uncut yellowed grass every where.
            In front of you are spikey thorn bushes, vaguely covering
            the murky windows of the mansion. You cannot see much through the
            window.
        
            A row of creaking, menacing trees marks the right wall of the garden.
            You can go back to the front door to the left.
            
            
        """ 
}

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

    playing = True
    while playing:
        print(dedent(room["description"]))
        print("What would you like to do?")
        response = input("> ")

        try:
            parsed = pp.parse(response, Answer)
        except:
            print("sorry game is not working try again!")
            continue
        
        if parsed.verb == "run" and parsed.noun == "away":
            print("This is probably a good idea, but that's the end of the game. Bye!")
            game_over()
            playing = False
        elif parsed.verb in ['run', 'walk', 'go', 'move']:
            exits = room["exits"]
            if parsed.noun in exits:
                room = rooms[exits[parsed.noun]]
            else:
                print("Sorry you can't go that way")


if __name__ == '__main__':
    main()
