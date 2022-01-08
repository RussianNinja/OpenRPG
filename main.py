
from ninjaRPG.game import Game
from ninjaRPG.toolser import clear_screen

game = Game()

def start():
    clear_screen()
    print("Это моя первая игра на Питоне")
    print("Прошу прощения за ошибки и корявый код")
    print('############################')
    print("#Добро пожаловть в OpenRPG!#")
    print('############################')
    game.main_menu()

if __name__ == '__main__':
    start()
    print("Game END!")
