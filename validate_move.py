"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def validate_move(board, character, user_input):
    """
    validate if diredtion inputed is a valid move for character on board

    :param user_input: string
    :param board: dictionary representing play space
    :param character: dictionary representing user character
    :precondition: character must be on valid position on board
                   user_input must be a valid string, only '1' '2' '3' '4'
                   board is dictionary with keys being tuples representing location on board
    :postcondition: correctly calculates whether new character location would be valid on given board then return
                    boolean value where True is valid and False is invalid
    :return: boolean value; True if valid, False if invalid

    >>> character_1 = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> user_input_1 = '1'
    >>> validate_move(board_1, character_1, user_input_1)
    False
    >>> character_2 = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> board_2 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> user_input_2 = '4'
    >>> validate_move(board_2, character_2, user_input_2)
    True
    """

    match user_input:
        case 'north':  # north
            if character['Y-coordinate'] == 0:
                return False
        case 'east':  # east
            if character['X-coordinate'] == max(board.keys())[1]:
                return False
        case 'west':  # west
            if character['X-coordinate'] == 0:
                return False
        case 'south':  # south
            if character['Y-coordinate'] == max(board.keys())[0]:
                return False
    return True


def main():
    pass


if __name__ == "__main__":
    main()
