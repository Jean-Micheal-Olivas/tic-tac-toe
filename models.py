from typing import List

from utils.console import clear_screen
from utils.validation import invalid_str_length


class Player:
    # name should not be more than 12 characters
    NAME_LENGTH = 12

    def __init__(self, name: str, *, legend: str) -> None:
        # legend should only be 1 character

        # Will raise exception if length is invalid
        self.name = name
        self.legend = legend

    def __str__(self) -> str:
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if invalid_str_length(value, Player.NAME_LENGTH):
            raise ValueError(f'Name should not be more than {Player.NAME_LENGTH}.')

        if value == '':
            raise ValueError('Name cannot be empty.')

        self._name = value

    @property
    def legend(self):
        return self._legend

    @legend.setter
    def legend(self, value):
        if invalid_str_length(value, 1):
            raise ValueError('Legend should only be 1 character.')

        if value == '':
            raise ValueError('Legend cannot be empty.')

        self._legend = value


class GameManager:
    """
    Handles all game controls.
    """
    PLAYER_COUNT = 2

    def __init__(self) -> None:
        self.active: bool = True
        self.players: List[Player] = []

    def start(self) -> None:
        # Start the game
        self.__init_players()
        self.__display_status_bar()

    def quit(self):
        # Quit the game
        pass

    def __display_status_bar(self) -> None:
        clear_screen()
        print('Players:')
        for player in self.players:
            print(f'{player.name}: {player.legend}')

    def __init_players(self):
        while len(self.players) < GameManager.PLAYER_COUNT:

            player_info = {
                'name': '',
                'legend': '',
            }

            while True:
                player_info['name'] = input(f'Enter player {len(self.players) + 1} name: ')
                player_info['legend'] = input(f'Enter player {len(self.players) + 1} legend: ')

                try:
                    self.players.append(Player(**player_info))
                except ValueError as e:
                    print(e)
                else:
                    break
