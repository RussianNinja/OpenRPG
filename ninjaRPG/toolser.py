import os
import sys


def clear_screen(self):
    if sys.platform=='win32':
        os.system('cls')
    else: os.system('clear')