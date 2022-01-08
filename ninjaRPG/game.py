import os
import sys



class Game:
    def __init__(self):
        pass

    def clear_screen(self):
        if sys.platform=='win32':
            os.system('cls')
        else: os.system('clear')

    def main_menu(self):
        print("Введите комманду меню")