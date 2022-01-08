import json

from toolser import clear_screen
from game import Game

def load_map(name_map):

    if name_map == 'educational_game':
        clear_screen()
        print(name_map)