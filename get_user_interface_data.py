"""
Tommy Ju
A01347715

Matthew
A01373290
"""


def get_user_interface_data(character, endpoint, enemies):
    """
    Retrieves game board coordinates necessary to create a GUI

    :param character: a dictionary representing the game character
    :param endpoint: a tuple representing the endpoint coordinates
    :param enemies: a list of tuples representing enemy coordinates
    :precondition: character must be a dictionary created by the make_character function
    :precondition: coordinates must be valid coordinates on the game board
    :postcondition: retrieve character, endpoint, and enemy coordinates for creating a game board
    :return: a dictionary representing each parameter's coordinates as a tuple(s)

    >>> some_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> some_endpoint = (4, 4)
    >>> some_enemies = [(1, 1), (2, 3)]
    >>> get_user_interface_data(some_character, some_endpoint, some_enemies)
    {'character': (0, 0), 'endpoint': (4, 4), 'enemies': [(1, 1), (2, 3)]}
    """
    game_board_data = dict()
    game_board_data["character"] = (character["X-coordinate"], character["Y-coordinate"])
    game_board_data["endpoint"] = endpoint
    game_board_data["enemies"] = enemies

    return game_board_data


def main():
    pass


if __name__ == "__main__":
    main()
