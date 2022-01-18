# import json
from ninjaRPG import toolser
from ninjaRPG.Character_Creator import create_char


def load_map(name_map):
    if name_map == 'educational_game':
        toolser.clear_screen()
    elif name_map == "new_game":
        toolser.clear_screen()
        create_char()
        