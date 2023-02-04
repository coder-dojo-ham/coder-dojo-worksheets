# In scratch everything is an object. Lets do that..
# No call backs!
import pypeg2 as pp
from textwrap import dedent
import re

from locations import locations, starting_location, location_items, game_intro_text

# This list has the allowable verbs, and their synonyms. The terminal (no synonym) must be here too for the system
# to recognise it as a verb
verb_synonyms = {
    "walk": "walk",
    "go": "walk",
    "run": "walk",
    "move": "walk",

    "hit": "hit",
    "punch": "hit",
    "kick": "kick",

    "take": "take",
    "get": "take",
    "pick": "take",

    "lift": "lift",

    "use": "use",
    "try": "use",

    "inspect": "inspect",
    "look": "inspect",
    "desc": "inspect",
    "describe": "inspect",

    "climb": "climb",
    "ascend": "climb",

    "open": "open",
    "unlock": "open",

    "inventory": "inventory",
    "inv": "inventory",

    "eat": "eat",
}

class Verb(pp.Keyword):
    verbs_p = [pp.K(verb) for verb in verb_synonyms.keys()]
    grammar = pp.Enum(*verbs_p)


class VerbExtra(pp.Keyword):
    grammar = pp.Enum(pp.K('at'), pp.K('in') )

directions = [
    "away",
    "up",
    "down",
    "forward",
    "forwards",
    "back",
    "backward",
    "backwards",
    "left",
    "right",
    "upwards",
    "downwards",
    "north",
    "east",
    "south",
    "west"
]

class Direction(pp.Keyword):
    directions_p = [pp.Keyword(item) for item in directions]
    grammar = pp.Enum(*directions_p)

direction_synonyms = {
    "forwards": "forward",
    "back": "backward",
    "backwards": "backward",
    "upwards": "up",
    "downwards": "down",
    "north": "forward",
    "east": "right",
    "south": "backward",
    "west": "left",
}


class Noun(pp.List):
   grammar = pp.some(pp.word)


class Filler(pp.Keyword):
    grammar = pp.Enum("the", "a", "an")


class Answer:
    grammar = [
        (pp.attr('verb', Verb), pp.ignore((pp.optional(VerbExtra), pp.optional(Filler),)),
            pp.optional(pp.attr('direction', Direction) ),
            pp.optional(pp.attr('noun', Noun)) ), # Verb and some nouns
        (pp.attr('direction', Direction),) # Noun only
    ]


import pytest

def parse_wrap(*args, **kwargs):
    __tracebackhide__ = True
    return pp.parse(*args, **kwargs)

def test_answer1():
    result = parse_wrap("run", Answer)
    assert result.verb == "run"

def test_answer2():
    result = parse_wrap("hit door", Answer)
    assert result.verb == "hit"
    assert result.noun == ["door"]

    result = parse_wrap("look at the door", Answer)
    assert result.verb == "look"
    assert result.noun == ["door"]

    result = parse_wrap("look at the withered plant", Answer)
    assert result.verb == "look"
    assert result.noun == ["withered", "plant"]

    result = parse_wrap("forward", Answer)
    assert result.direction == "forward"

    result = parse_wrap("climb up tree", Answer)
    assert result.verb     ==  "climb"
    assert result.direction == "up"
    assert result.noun      == ["tree"]


class GameOver(Exception):
    # Raise this to signal the game over condition
    pass


class Prop:
    def __init__(self, name, actions):
        print("Creating prop", name)
        self.name = name
        self.actions = actions

    def inspect(self):
        print(dedent(self.actions['inspect']['say']))


    def process_action_item(self, action_item):
        print(dedent(action_item['say']))
        effects = {

        }
        if action_item.get('add_item'):
            effects['add_item'] = action_item['add_item']
        if action_item.get('game_over', False):
            effects['game_over'] = True
        return effects

    def action(self, name):
        action_item = self.actions[name]
        return self.process_action_item(self)

    def item_action(self, noun, item):
        try:
            if self.actions[noun]['with_item']['item'] == item.name:
                action_item = self.actions[noun]['with_item']
                return self.process_action_item
        except KeyError:
            pass
        print('You cannot use {item} to {noun} with the {name}'.format(
            item=item, noun=noun, name=self.name
        ))

# Now the game types
class Player:
    def __init__(self):
        self.items = {
            "pocket lint": Prop("pocket lint", location_items["pocket lint"])
        }

    def show_inventory(self):
        print("In your possession you currently have:")
        for item in self.items:
            print(item)

    def add_item(self, item):
        print("Item added: ", item.name)
        self.items[item.name] = item

    def has_item(self, item_name):
        return item_name in self.items

class Location:
    def __init__(self, details):
        self.description = dedent(details['description'])
        self.exits = details.get('exits', {})
        props = details.get('props', {})
        self.props = dict(
            (prop_name, Prop(prop_name, prop_details))
            for prop_name, prop_details in props.items())
        items = details.get('items', {})
        self.items = dict(
            (item_name, Prop(item_name, item_details))
            for item_name, item_details in items.items())

        self.synonyms = details.get('synonyms', {})
        self.game_over = details.get('game_over', {})

    def get_prop(self, noun):
        try:
            noun = self.synonyms.get(noun, noun)
            return self.props[noun]
        except KeyError: # Depluralize
            noun = noun.strip('s')
            noun = self.synonyms.get(noun, noun)
            return self.props[noun]


    def enter(self):
        self.inspect()
        if self.game_over:
            raise GameOver()

    def inspect(self):
        print(self.description)


class Map:
    def __init__(self, locations):
        self.locations = {}
        # Set up the locations
        for name, location in locations.items():
            self.locations[name] = Location(location)
        self._location = None
        self.current_location = self.locations[starting_location]

    def enter_location_by_name(self, location_name):
        self.current_location = self.locations[location_name]

    @property
    def current_location(self):
        return self._location

    @current_location.setter
    def current_location(self, location):
        self._location = location
        location.enter()


class Game:
    def __init__(self):
        self.player = None
        self.map = None
        self.is_playing = False

    def run(self):
        self.player = Player()

        self.is_playing = True
        print(dedent(game_intro_text))
        self.map = Map(locations)

        while self.is_playing:
            print("\nWhat would you like to do?")
            try:
                response = input("> ")
            except EOFError:
                try:
                    self.map.current_location = self.map.locations['away']
                except GameOver:
                    pass
                self.game_over()
                return

            try:
                verb, noun, direction = self.parse_response(response)
            except:
                print("I don't know how to do that!")
                continue
            try:
                self.handle_response(verb, noun, direction)
            except GameOver:
                self.game_over()
                return

    def parse_response(self, response):
            parsed = pp.parse(response, Answer)
            verb, noun, direction = None, None, None
            if hasattr(parsed, 'verb'):
                verb = verb_synonyms.get(parsed.verb, parsed.verb)
                print("Verb", repr(verb))
            if hasattr(parsed, 'noun'):
                noun = ' '.join(parsed.noun)
                print("Noun", noun)
            if hasattr(parsed, 'direction'):
                direction = direction_synonyms.get(parsed.direction, parsed.direction)
                print("Direction", repr(direction))
            return verb, noun, direction

    def game_over(self):
        self.is_playing = False
        print(dedent("""\
            -------------------------------------------------------------------------------
                                    Game Over!
            -------------------------------------------------------------------------------
        """))

    def process_effects(self, prop, verb, effects):
            if effects.get('game_over'):
                raise GameOver()
            if effects.get('add_item'):
                item_name = effects['add_item']
                item = self.map.current_location.items[item_name]
                self.player.add_item(item)
            if effects.get('with_item'):
                if self.player.has_item(effects['with_item']['item']):
                    new_effects = prop.item_action(verb, effects['with_item']['item'])
                else:
                    new_effects = prop.no_item_action()
                self.process_effects(new_effects)

    def prop_action(self, verb, noun):
        if noun in self.player.items:
            prop = self.player.items[noun]
        else:
            prop = self.map.current_location.get_prop(noun)
        try:
            effects = prop.action(verb)
            self.process_effects(prop, verb, effects)
        except KeyError:
            print("I dont know how to do that.")

    def handle_response(self, verb, noun, direction):
        if verb=="walk" and direction=="away":
            self.map.current_location = self.map.locations['away']
            self.game_over()
            return
        if direction in self.map.current_location.exits:
            self.map.enter_location_by_name(self.map.current_location.exits[direction])
            return
        if verb == "inspect" and (noun == ["room"] or noun is None):
            self.map.current_location.inspect()
            return
        if verb == "inventory":
            self.player.show_inventory()
            return
        if noun and verb:
            try:
                self.prop_action(verb, noun)
                return
            except KeyError:
                pass
        if noun:
            print("I don't see a '{}'".format(noun))
        else:
            print("I didn't understand")

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
