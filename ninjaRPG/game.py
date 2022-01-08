from ninjaRPG.ninja_scens_manager import load_map
from ninjaRPG.user_input_parser import user_comand


class Game:
    def __init__(self):
        pass

    def main_menu(self):
        print('############################')
        print("#      -Обучающая игра-    #")
        print("#       -Новая игра-       #")
        print("#          -Выход-         #")
        print('############################')
        print("#  -Введите комманду меню- #")
        choice = user_comand("> ").lower()
        if choice == "обучающая игра":
            load_map('educational_game')
