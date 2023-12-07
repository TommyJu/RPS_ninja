"""
Tommy Ju
A01347715
Matthew
A01373290
"""


def check_if_endpoint_reached(character: dict, board: dict) -> bool:
    """
    Determine if the character has reached the endpoint of the board

    The endpoint of the boards is the bottom left always.

    :param character: dictionary representing the player character
    :param board: dictionary representing the game board
    :preconcition: character is a dictionary with keys "X-coordiante" and "Y-coordinate" with integer values
                   Board is dictionary with tuple keys
    :postcondition: correctly determines if character is in endpoint square
                    True if in endpoint, False if not in endpoint
    :return: Boolean value representing if character is at the endpoint
    """
    return (character["X-coordinate"], character["Y-coordinate"]) == max(board.keys())


def main():
    pass


if __name__ == "__main__":
    main()
