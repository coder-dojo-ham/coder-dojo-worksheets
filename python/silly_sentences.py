from random import choice

people = ["Mummy", "Daddy", "Bob", "Dave" , "Beth"]

# add some wholesome silly thing words
silly_things = ["cutie" , "goat", "rusty spoon",
                "great daft banana", "stuffy bore",                 
                "absolute genius", "great fairy", "silly sausage"]

for person in people:
    print("{person} is a {thing}".format(person=person, thing=choice(silly_things)))
