"""
Tommy Ju
A01347715

Matthew
A01373290
"""


def describe_current_location(game_board, character):
    """
    Compare character and game board coordinates to find the room description

    :param game_board: a dictionary representing the game board
    :param character: a dictionary representing the character
    :precondition: game_board must be a dictionary created by the make_board function
    :precondition: character must be a dictionary created by the make_character function
    :precondition: character must be in a valid position on the game board
    :postcondition: prints the room description string value using character and game_board coordinates
    """
    character_coordinates = (character["X-coordinate"], character["Y-coordinate"])
    print("Your location:", game_board[character_coordinates], character_coordinates)


def main():
    pass


if __name__ == "__main__":
    main()
