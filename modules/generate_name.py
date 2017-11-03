import random
import sys

from data import names
from data import surnames

def get_name(race):
    return name(race) + " " + surname(race)

def name(race):
    if race == 'orc':
        return random.choice(names.orc)
    elif race == 'elf':
        return random.choice(names.elf)
    elif race == 'human':
        return random.choice(names.human)
    elif race == 'undead':
        return random.choice(names.undead)
    elif race == 'troll':
        return random.choice(names.troll)
    else:
        sys.exit(1)

def surname(race):
    return random.choice(surnames.list)