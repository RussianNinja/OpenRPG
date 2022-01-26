from ninjaRPG.scens_manager import load_map
from ninjaRPG.user_input_parser import user_comand
from ninjaRPG.toolser import exit_game


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
        elif choice == "новая игра":
            load_map("new_game")
        elif choice == "выход":
            exit_game()

