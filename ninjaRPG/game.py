from ninjaRPG.user_input_parser import user_comand
import scens_manager


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
            scens_manager.load_map(choice)