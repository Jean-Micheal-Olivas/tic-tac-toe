from os import name as os_name
from os import system


def clear_screen() -> None:
    if os_name == 'nt':
        system('cls')
    else:
        system('clear')
