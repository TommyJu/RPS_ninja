"""
Tommy Ju
A01347715

Matthew
A01373290
"""
import random


def make_board(rows, columns):
    """
    Create a dictionary of coordinate keys and description values representing a game board

    The origin (0, 0) is in the top left corner of the game board

    :param rows: an integer representing the number of rows for the game board
    :param columns: an integer representing the number of columns for the game board
    :precondition: rows and columns must be non-zero integers >= 2
    :postcondition: creates a game board dictionary with the specified number of rows and columns
    :return: a dictionary representing game board coordinates and random room descriptions
    """
    room_descriptions = [
        "A haunted mansion",
        "An eerie forest",
        "A deserted village",
        "A mountain trail",
        "A vast ravine",
        "A dark tunnel",
        "An abandoned farm"
    ]

    game_board = {(row, column): random.choice(room_descriptions) for row in range(rows) for column in range(columns)}
    return game_board


def main():
    pass


if __name__ == "__main__":
    main()
